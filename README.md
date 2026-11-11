# ИИ-сервер за вечер

Статический сайт-кейс (HTML/CSS/JS, без сборщиков) для GitHub Pages: как арендовать сервер, поставить Claude Code и подключить Telegram-бота.

- `index.html` — лендинг, `example.html` — живой пример, `steps/01..07.html` — шаги.
- Страницы генерирует `python3 tools/build_site.py` (код бота и служба systemd — в `tools/bot_example.py`, `tools/tgbot.service`).
- Партнёрские кнопки на шаге 1 — заглушки (`data-partner="hosting-N"`, `href="#"`): подставить ссылки в `tools/build_site.py` и пересобрать.
