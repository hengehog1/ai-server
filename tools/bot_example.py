import asyncio
import os
import shutil
from pathlib import Path

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
OWNER_ID = int(os.environ["OWNER_ID"])
WORKDIR = Path.home() / "workspace"
CLAUDE = os.environ.get("CLAUDE_BIN") or shutil.which("claude") or str(Path.home() / ".local/bin/claude")
WORKDIR.mkdir(exist_ok=True)


async def ask_claude(text: str, fresh: bool) -> str:
    cmd = [CLAUDE, "-p", "--allowedTools", "Read,Glob,Grep"]
    if not fresh:
        cmd.append("--continue")
    proc = await asyncio.create_subprocess_exec(
        *cmd, cwd=WORKDIR,
        stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    try:
        out, err = await asyncio.wait_for(proc.communicate(text.encode()), timeout=600)
    except asyncio.TimeoutError:
        proc.kill()
        return "Слишком долго думаю, попробуй задачу попроще."
    if proc.returncode:
        return "Ошибка Claude Code:\n" + err.decode()[-500:]
    return out.decode().strip() or "(пустой ответ)"


async def cmd_id(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Твой Telegram ID: {update.effective_user.id}")


async def cmd_new(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    ctx.bot_data["fresh"] = True
    await update.message.reply_text("Начинаем новый разговор.")


async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return  # чужим не отвечаем вообще
    await update.message.chat.send_action("typing")
    answer = await ask_claude(update.message.text, ctx.bot_data.pop("fresh", False))
    for i in range(0, len(answer), 4000):
        await update.message.reply_text(answer[i:i + 4000])


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("id", cmd_id))
    app.add_handler(CommandHandler("new", cmd_new))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.run_polling()
