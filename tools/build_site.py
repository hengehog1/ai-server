# Генератор статического сайта «ИИ-сервер за вечер». Запуск: python3 tools/build_site.py
import html, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GAME = "https://194-87-6-96.sslip.io:8443/"
APK = "https://194-87-6-96.sslip.io:8443/download/neuroquest.apk"
TG = "https://t.me/neuroquest_game"
GH = "https://hengehog1.github.io/neuroquest"
YT = "https://www.youtube.com/@Neuroquest_game"
AFF = "Некоторые ссылки партнёрские."
E = html.escape


def code(text, cap=""):
    c = f'<span class="cap">{E(cap)}</span>' if cap else ""
    return f'<div class="code">{c}<button class="copy" type="button">Копировать</button><pre><code>{E(text.strip(chr(10)))}</code></pre></div>'


def i(s):
    return f'<code class="i">{E(s)}</code>'


def note(s):
    return f'<div class="note">{s}</div>'


# ---------- тексты, написанные ChatGPT (правка: мелкая) ----------
HOME = dict(
    h1="Свой ИИ-сервер за один вечер",
    sub="Арендуй недорогой сервер, установи Claude Code и общайся со своим ИИ-помощником через Telegram прямо с телефона. Разберём всё по шагам, даже если ты никогда не работал с Linux.",
    who=["Новичкам, которые хотят разобраться с ИИ", "Тем, кто хочет управлять ИИ с телефона", "Тем, кто мечтает о собственном круглосуточном ИИ-помощнике"],
    live="На таком сервере у автора сайта круглосуточно работают Telegram-боты, связанные с Claude Code. Они помогают выполнять задачи, писать код и заниматься проектами, даже когда основной компьютер выключен. Автор управляет помощниками через Telegram и постепенно расширяет их возможности.",
    byte="Не знаешь Linux? Отлично, значит, начнём с самого интересного! 🤖",
)
STEPS = [
 dict(t="Выбор сервера", short="Выбираем недорогой сервер, который станет домом для твоего ИИ.",
  why="Сервер — это удалённый компьютер, который работает в дата-центре и доступен через интернет. Тебе не понадобится покупать дорогое оборудование или держать домашний компьютер постоянно включённым. Для начала достаточно недорогого виртуального сервера с Linux, подходящего под требования Claude Code.",
  got="У тебя появится собственный сервер с IP-адресом и данными для подключения. Это основа будущего ИИ-помощника.",
  errs=["Покупать слишком дорогой тариф", "Выбирать сервер без проверки характеристик", "Забывать про стоимость продления аренды"],
  byte="Не покупай космический корабль, когда нам пока нужен велосипед с интернетом! 🚀"),
 dict(t="Первый вход по SSH", short="Подключаемся к серверу и выполняем первые команды Linux.",
  why="SSH — это способ безопасно управлять удалённым компьютером через командную строку. Вместо привычных окон и кнопок ты будешь вводить короткие команды. Я покажу, что они означают и как понять, что всё получилось.",
  got="Ты самостоятельно войдёшь на сервер, проверишь его работу и выполнишь первые команды. Незнакомый чёрный экран перестанет казаться страшным.",
  errs=["Неправильно вводить IP-адрес", "Путать пароль сервера с паролем личного компьютера", "Считать отсутствие символов при вводе пароля ошибкой"],
  byte="Поздравляю! Теперь ты управляешь компьютером, до которого даже не нужно дотрагиваться! 🤖"),
 dict(t="Защита сервера", short="Закрываем лишние двери и защищаем сервер от посторонних.",
  why="Сервер постоянно доступен через интернет, поэтому его безопасность нельзя откладывать. Мы создадим отдельного пользователя, настроим вход по SSH-ключу, обновления и сетевой экран. Всё сделаем последовательно, чтобы случайно не потерять доступ.",
  got="Сервер получит базовую защиту от распространённых угроз. Ты научишься безопаснее управлять им и поймёшь, почему нельзя публиковать пароли и секретные ключи.",
  errs=["Оставлять простой пароль", "Отключать старый способ входа до проверки нового", "Закрывать SSH-порт в сетевом экране без проверки доступа"],
  byte="Прежде чем поселить ИИ, поставим крепкую дверь и хороший замок! 🔐"),
 dict(t="Установка Claude Code", short="Устанавливаем Claude Code и запускаем первого ИИ-помощника.",
  why="Claude Code — это ИИ-инструмент, который умеет работать с кодом, файлами и проектами. Мы установим его официальным способом, подключим через доступный способ авторизации и проверим на простом задании. Для использования потребуется подходящая подписка или оплачиваемый API-доступ.",
  got="Claude Code будет работать на твоём сервере и сможет помогать с задачами в пределах предоставленных разрешений. Ты отправишь ему первый запрос и увидишь результат.",
  errs=["Использовать устаревшие инструкции установки", "Путать подписку Claude с API-оплатой", "Давать ИИ доступ ко всему серверу без необходимости"],
  byte="А вот и мозги нашей операции! Только не забудь: даже умному ИИ нужны понятные задачи! 🧠"),
 dict(t="Telegram-бот для связи", short="Подключаем Telegram, чтобы писать своему ИИ с телефона.",
  why="Необязательно каждый раз открывать терминал, чтобы обратиться к помощнику. Мы создадим Telegram-бота через официальный BotFather и подключим его к серверному приложению, которое передаёт сообщения Claude Code. Доступ ограничим твоим Telegram ID, а секретный токен сохраним отдельно от кода.",
  got="Ты сможешь отправлять своему ИИ задания из Telegram и получать ответы прямо на телефон. Бот станет удобным интерфейсом для работы с сервером, а не открытым помощником для посторонних.",
  errs=["Публиковать токен Telegram-бота", "Не ограничивать список разрешённых пользователей", "Разрешать выполнение любых команд без проверки"],
  byte="Теперь твой ИИ буквально в кармане! Главное — не отправляй ему случайно список покупок вместо задания! 📱"),
 dict(t="Автозапуск и логи", short="Настраиваем автоматическую работу бота и проверку ошибок.",
  why="Если закрыть терминал, неправильно запущенная программа может остановиться. Мы настроим автозапуск через systemd, чтобы бот запускался вместе с сервером и перезапускался после сбоя. А ещё научимся читать логи — записи о работе программы, которые помогают находить ошибки.",
  got="Telegram-бот сможет работать круглосуточно без открытого терминала на твоём компьютере, пока сервер и необходимые сервисы доступны. Ты будешь знать, как проверить состояние бота, найти причину сбоя и перезапустить его.",
  errs=["Запускать бота только в обычном терминале", "Не проверять состояние службы после перезагрузки", "Сохранять секретные данные в открытых логах"],
  byte="Теперь помощник умеет работать без твоего постоянного присмотра. Но иногда даже роботам нужен техосмотр! ⚙️"),
 dict(t="НЕЙРОКВЕСТ и сообщество", short="Учимся лучше общаться с ИИ через игру и сообщество.",
  why="Установить ИИ — только половина дела. Важно научиться правильно ставить задачи, формулировать запросы и проверять результаты. В бесплатной игре НЕЙРОКВЕСТ ты сможешь тренировать эти навыки в игровом формате, а в Telegram-сообществе — обмениваться опытом, задавать вопросы и находить новые идеи.",
  got="У тебя будет не только работающий ИИ-помощник, но и возможность развивать навыки общения с нейросетями. Продолжай обучение в НЕЙРОКВЕСТ, делись результатами в сообществе и пробуй собственные проекты.",
  errs=["Ожидать, что ИИ сам поймёт любую задачу", "Слепо доверять каждому ответу нейросети", "Переставать экспериментировать после первой неудачи"],
  byte="Сервер запущен, ИИ подключён, а наше приключение только начинается! Увидимся в НЕЙРОКВЕСТ! 🎮"),
]

# ---------- содержимое шагов (команды проверены по документации / на реальном сервере) ----------
def body(n):
    if n == 1:
        return f"""
<h2>Что нужно от сервера</h2>
<table><tr><th>Параметр</th><th>Базовый вариант</th><th>«Посильнее» (с запасом)</th></tr>
<tr><td>Система</td><td>Ubuntu 24.04</td><td>Ubuntu 24.04</td></tr>
<tr><td>Процессор</td><td>2 ядра</td><td>4 ядра</td></tr>
<tr><td>Память (ОЗУ)</td><td>4 ГБ</td><td>8 ГБ</td></tr>
<tr><td>Диск</td><td>40 ГБ SSD</td><td>80 ГБ SSD</td></tr></table>
{note("Claude Code по требованиям нужно <b>минимум 4 ГБ ОЗУ</b> и Ubuntu 20.04+ — поэтому базовый вариант именно такой. Вариант «посильнее» пригодится, если захочешь запускать на сервере несколько ботов и проектов.")}
<h2>На что смотреть при выборе</h2>
<ul><li><b>Тип:</b> виртуальный сервер (VPS) на Linux, без «безлимита» и сомнительных акций.</li>
<li><b>Образ системы:</b> в списке должна быть Ubuntu 24.04.</li>
<li><b>Оплата:</b> выбирай хостинг, который принимает официальные способы оплаты в твоей стране. Сравни цену за месяц и условия продления.</li>
<li><b>Доступ:</b> после покупки тебе дадут IP-адрес, имя пользователя (обычно <code class="i">root</code>) и пароль или SSH-ключ.</li>
<li><b>Расположение:</b> город дата-центра не критичен, главное — стабильная связь.</li></ul>
<h2>Где взять сервер</h2>
<p>Ниже — хостинги, которые мы рассматриваем. Кнопки появятся, как только мы добавим проверенные ссылки.</p>
<div class="partners">
<a class="btn small ghost" href="#" data-partner="hosting-1" rel="sponsored nofollow">Хостинг 1 — скоро</a>
<a class="btn small ghost" href="#" data-partner="hosting-2" rel="sponsored nofollow">Хостинг 2 — скоро</a>
<a class="btn small ghost" href="#" data-partner="hosting-3" rel="sponsored nofollow">Хостинг 3 — скоро</a></div>
<h2>Что запомнить после покупки</h2>
<p>Сохрани в надёжном месте три вещи: <b>IP-адрес</b>, <b>логин</b> и <b>пароль</b> (или ключ). Никому их не показывай и не публикуй в чатах и на скриншотах.</p>"""
    if n == 2:
        return f"""
<h2>Откуда подключаться</h2>
<ul><li><b>Windows 10/11:</b> открой программу «Терминал» или PowerShell (поиск по меню «Пуск»).</li>
<li><b>macOS и Linux:</b> открой «Терминал».</li>
<li><b>С телефона:</b> подойдёт приложение Termius или похожее, но для первого раза удобнее компьютер.</li></ul>
<h2>Подключение</h2>
<p>Замени <code class="i">203.0.113.10</code> на IP-адрес своего сервера из письма от хостинга:</p>
{code("ssh root@203.0.113.10")}
<p>При первом входе система спросит про отпечаток сервера — напиши <code class="i">yes</code>. Потом введи пароль. <b>Пока ты печатаешь пароль, символы на экране не появляются</b> — это нормально.</p>
<h2>Первые команды</h2>
{code("lsb_release -a", "Какая система")}
{code("nproc", "Сколько ядер")}
{code("free -h", "Сколько памяти")}
{code("df -h /", "Сколько места на диске")}
<p>Должно получиться: в ответе есть <i>Ubuntu 24.04</i>, число ядер и размеры памяти и диска, которые ты выбирал. Чтобы выйти с сервера, набери <code class="i">exit</code>.</p>
{note("Если команда не сработала — не пугайся: ошибка в консоли обычно говорит, что не так. Скопируй её и спроси у Claude или у нас в сообществе.")}"""
    if n == 3:
        return f"""
{note("<b>Главное правило этого шага:</b> не закрывай окно, где ты уже вошёл на сервер, пока не проверишь новый вход в <b>отдельном</b> окне. Тогда ты не потеряешь доступ.")}
<h2>1. Обновляем систему</h2>
{code("apt update && apt -y upgrade")}
<h2>2. Создаём обычного пользователя</h2>
<p>Работать от имени <code class="i">root</code> опасно: он может всё и без вопросов. Создадим пользователя <code class="i">ai</code> (имя любое):</p>
{code("adduser ai")}
{code("usermod -aG sudo ai")}
<h2>3. Вход по SSH-ключу</h2>
<p>Ключ — это как цифровой замок из двух частей. Одна часть остаётся у тебя, другая — на сервере. <b>На своём компьютере</b> (не на сервере) выполни:</p>
{code("ssh-keygen -t ed25519")}
{code("ssh-copy-id ai@203.0.113.10")}
<p><b>Если у тебя Windows</b>, команды <code class="i">ssh-copy-id</code> там нет. Вместо неё выполни в PowerShell одну длинную команду:</p>
{code('type $env:USERPROFILE\\.ssh\\id_ed25519.pub | ssh ai@203.0.113.10 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"')}
<p>Теперь открой <b>новое окно терминала</b> и проверь вход:</p>
{code("ssh ai@203.0.113.10")}
<p>Если вошёл без пароля от сервера (мог попросить только пароль от ключа) — всё хорошо.</p>
<h2>4. Отключаем вход по паролю и под root</h2>
<p>Сначала убедись, что вход по ключу работает. Затем на сервере, уже под пользователем <code class="i">ai</code>:</p>
{code("sudo nano /etc/ssh/sshd_config.d/00-hardening.conf")}
<p>Имя файла начинается с <code class="i">00-</code> не случайно: настройки читаются по порядку, и первое значение побеждает. Так наша защита не перебьётся настройками хостинга. Впиши в файл две строки, сохрани (<code class="i">Ctrl+O</code>, Enter) и выйди (<code class="i">Ctrl+X</code>):</p>
{code("PasswordAuthentication no\nPermitRootLogin no")}
{code("sudo sshd -t && sudo systemctl reload ssh")}
<p>Первая команда проверяет настройки, вторая применяет их. Снова проверь вход в новом окне.</p>
<h2>5. Сетевой экран (ufw)</h2>
{code("sudo ufw allow OpenSSH\nsudo ufw enable")}
{code("sudo ufw status")}
<p>Должно быть: статус <i>active</i>, и правило для OpenSSH разрешено.</p>
<h2>6. Защита от подбора пароля (fail2ban)</h2>
{code("sudo apt install -y fail2ban\nsudo systemctl enable --now fail2ban")}
{code("sudo fail2ban-client status")}
<p>Fail2ban сам временно блокирует тех, кто часто ошибается при входе. Это отсекает большинство автоматических атак.</p>"""
    if n == 4:
        return f"""
<h2>Что нужно заранее</h2>
<ul><li>Ubuntu 20.04 и новее, минимум 4 ГБ ОЗУ и доступ в интернет (это требования из официальной документации).</li>
<li>Аккаунт Claude с доступом к Claude Code: подписка Pro, Max и выше, Team или Console с API-оплатой. Бесплатного тарифа для Claude Code недостаточно.</li>
<li>Страна из <a href="https://www.anthropic.com/supported-countries" rel="noopener">списка поддерживаемых</a>.</li></ul>
{note("Оплачивай подписку только официальными способами, доступными в твоей стране. Подробные инструкции и ответы на вопросы — в нашем <a href=\"" + TG + "\" rel=\"noopener\">Telegram-сообществе</a>.")}
<h2>1. Установка</h2>
<p>Подключись к серверу под пользователем <code class="i">ai</code> (не root и без sudo) и выполни официальную команду установки:</p>
{code("curl -fsSL https://claude.ai/install.sh | bash")}
<p>Установщик не показывает прогресс — это нормально. Когда он закончится, <b>закрой терминал и подключись заново</b>, чтобы система увидела новую программу.</p>
<h2>2. Проверка</h2>
{code("claude --version")}
{code("claude doctor")}
<p>Должно получиться: первая команда печатает номер версии, вторая сообщает, что установка в порядке. Если пишет «command not found», подключись к серверу заново или посмотри раздел про PATH в <a href="https://code.claude.com/docs/en/troubleshoot-install" rel="noopener">официальной документации</a>.</p>
<h2>3. Вход в аккаунт</h2>
<p>Создай папку для первых экспериментов и запусти Claude Code в ней:</p>
{code("mkdir -p ~/workspace && cd ~/workspace && claude")}
<p>Claude Code покажет ссылку для входа. Открой её в браузере на компьютере или телефоне, войди в свой аккаунт и вставь полученный код в терминал.</p>
<h2>4. Первый запрос</h2>
<p>Напиши прямо в Claude Code что-нибудь простое:</p>
{code("Создай файл hello.txt с приветствием и покажи, что в нём")}
<p>Claude Code попросит разрешение на создание файла. Прочитай, что он собирается сделать, и разреши. Выйти из программы: <code class="i">/exit</code> или два раза <code class="i">Ctrl+C</code>.</p>
{note("Работай в отдельной папке (<code class=\"i\">~/workspace</code>), а не в корне сервера, и не давай разрешений «на всё» без необходимости. Claude Code обновляется сам в фоне.")}"""
    if n == 5:
        return f"""
<h2>Как это устроено</h2>
<p>Ты пишешь боту в Telegram → бот на сервере передаёт текст Claude Code → ответ возвращается в чат. Бот отвечает <b>только тебе</b>: чужие сообщения он молча игнорирует.</p>
<h2>1. Создаём бота</h2>
<ol><li>В Telegram найди официального бота <b>@BotFather</b> и отправь ему <code class="i">/newbot</code>.</li>
<li>Придумай название и имя бота (оканчивается на <i>bot</i>).</li>
<li>BotFather пришлёт <b>токен</b> — длинную строку. Это пароль от бота: никому не показывай и не публикуй.</li></ol>
<h2>2. Готовим папку и окружение</h2>
{code("mkdir -p ~/bot && cd ~/bot\nsudo apt install -y python3-venv\npython3 -m venv venv\n./venv/bin/pip install python-telegram-bot")}
<h2>3. Файл с секретами</h2>
<p>Токен хранится отдельно от кода, в файле <code class="i">.env</code>. Сначала оставь <code class="i">OWNER_ID=0</code> — узнаем свой ID на следующем шаге.</p>
{code("nano ~/bot/.env")}
{code("TELEGRAM_BOT_TOKEN=сюда_токен_от_BotFather\nOWNER_ID=0")}
{code("chmod 600 ~/bot/.env")}
<h2>4. Код бота</h2>
<p>Создай файл <code class="i">~/bot/bot.py</code> и вставь в него код целиком:</p>
{code("nano ~/bot/bot.py")}
{code((ROOT / 'tools' / 'bot_example.py').read_text(encoding='utf-8'), "bot.py")}
<p>Что делает код: команда <code class="i">/id</code> показывает твой Telegram ID; любое обычное сообщение от владельца уходит в <code class="i">claude -p</code> (режим «ответь и выйди»); по умолчанию Claude Code может только <b>читать</b> файлы (<code class="i">Read, Glob, Grep</code>) — так безопасно начинать. Команда <code class="i">/new</code> начинает новый разговор.</p>
<h2>5. Узнаём свой ID и запускаем</h2>
{code("cd ~/bot && set -a && . ./.env && set +a && ./venv/bin/python bot.py")}
<p>Напиши боту в Telegram <code class="i">/id</code> — он ответит числом. Останови бота (<code class="i">Ctrl+C</code>), впиши число в <code class="i">.env</code> вместо <code class="i">0</code> и запусти снова. Теперь напиши боту любой вопрос — например, «что лежит в папке?».</p>
{note("Хочешь, чтобы бот мог ещё и создавать файлы и запускать команды? Добавляй нужные инструменты в <code class=\"i\">--allowedTools</code> по одному и только когда понимаешь, что они делают. Не выдавай боту разрешение на всё сразу.")}"""
    if n == 6:
        svc = (ROOT / 'tools' / 'tgbot.service').read_text(encoding='utf-8')
        return f"""
<h2>1. Служба systemd</h2>
<p>systemd — это «диспетчер» сервера: он запускает программы при старте и перезапускает упавшие. Создай файл службы:</p>
{code("sudo nano /etc/systemd/system/tgbot.service")}
<p>Вставь в него (если у тебя другое имя пользователя, замени <code class="i">ai</code> и пути):</p>
{code(svc, "tgbot.service")}
<h2>2. Включаем</h2>
{code("sudo systemctl daemon-reload\nsudo systemctl enable --now tgbot")}
{code("systemctl status tgbot")}
<p>Должно быть: <i>active (running)</i> зелёным цветом. Выйти из просмотра статуса: <code class="i">q</code>.</p>
<h2>3. Логи — «дневник» программы</h2>
{code("journalctl -u tgbot -n 50 --no-pager", "Последние 50 строк")}
{code("journalctl -u tgbot -f", "Смотреть в реальном времени (выход: Ctrl+C)")}
<h2>4. Управление</h2>
{code("sudo systemctl restart tgbot")}
{code("sudo systemctl stop tgbot")}
<h2>5. Проверка перезагрузки</h2>
<p>Самый честный тест: перезагрузи сервер и убедись, что бот сам ожил.</p>
{code("sudo reboot")}
<p>Подожди минуту, подключись снова и проверь <code class="i">systemctl status tgbot</code>. Или просто напиши боту в Telegram.</p>
{note("В логи не должны попадать токены и пароли: не печатай их в коде и не вставляй такие строки в чаты, когда просишь помощи.")}"""
    if n == 7:
        return f"""
<h2>Игра, которая учит общаться с ИИ</h2>
<p><b>НЕЙРОКВЕСТ</b> — бесплатная игра, где ты строишь свою ИИ-корпорацию вместе с роботом БАЙТом, проходишь миссии и тренируешься формулировать запросы к нейросетям.</p>
<div class="partners"><a class="btn" href="{GAME}" rel="noopener">▶ Играть в браузере</a>
<a class="btn ghost" href="{APK}" rel="noopener">📱 Скачать APK для Android</a></div>
<h2>Сообщество</h2>
<p>В Telegram-сообществе делимся опытом, отвечаем на вопросы по серверу, Claude Code и ботам.</p>
<div class="partners"><a class="btn ghost" href="{TG}" rel="noopener">🤖 Telegram-сообщество</a>
<a class="btn ghost" href="{YT}" rel="noopener">▶ YouTube-канал</a>
<a class="btn ghost" href="{GH}" rel="noopener">💻 GitHub</a></div>
<h2>Что дальше</h2>
<ul><li>Дай боту разрешение на запись файлов в <code class="i">~/workspace</code> и попроси сделать небольшой проект.</li>
<li>Настрой резервные копии и следи за обновлениями системы: <code class="i">sudo apt update && sudo apt upgrade</code>.</li>
<li>Расскажи в сообществе, что у тебя получилось.</li></ul>"""
    return ""


# ---------- шаблоны страниц ----------
def head(title, desc, depth):
    p = "../" * depth
    return f"""<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#070b1a"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="{p}img/byte-happy.webp"><link rel="stylesheet" href="{p}css/style.css"></head><body>"""


def top(depth):
    p = "../" * depth
    return f"""<header class="top"><div class="wrap"><a class="logo" href="{p}index.html">ИИ-сервер <b>за вечер</b></a>
<nav><a href="{p}index.html#steps">Шаги</a><a href="{p}example.html">Живой пример</a><a href="{p}index.html#nq">НЕЙРОКВЕСТ</a><a class="cta" href="{p}steps/01.html">Начать</a></nav></div></header>"""


def foot(depth):
    p = "../" * depth
    return f"""<footer><div class="wrap">Сайт сделан в проекте <a href="{GAME}" rel="noopener">НЕЙРОКВЕСТ</a> · <a href="{TG}" rel="noopener">Telegram</a> · <a href="{YT}" rel="noopener">YouTube</a> · <a href="{GH}" rel="noopener">GitHub</a>
<div class="aff">{AFF}</div></div></footer><script src="{p}js/main.js" defer></script></body></html>"""


def diagram():
    return """<svg viewBox="0 0 560 330" role="img" aria-label="Схема: телефон, Telegram, бот на сервере, Claude Code, файлы" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#00e5ff"/></marker>
<filter id="g"><feGaussianBlur stdDeviation="3"/></filter></defs>
<rect x="150" y="14" width="400" height="300" rx="18" fill="#0d1430" stroke="#a6ff00" stroke-dasharray="6 5"/>
<text x="168" y="40" fill="#a6ff00" font-size="15" font-family="system-ui" font-weight="700">Сервер Ubuntu (работает 24/7)</text>
<g font-family="system-ui" font-size="15" fill="#e8ecff" text-anchor="middle">
<rect x="8" y="110" width="116" height="90" rx="14" fill="#111a3a" stroke="#00e5ff"/><text x="66" y="150">Ты</text><text x="66" y="172" font-size="13" fill="#9aa7d6">Telegram</text>
<rect x="180" y="60" width="150" height="70" rx="14" fill="#111a3a" stroke="#00e5ff"/><text x="255" y="92">Бот (systemd)</text><text x="255" y="112" font-size="13" fill="#9aa7d6">принимает чат</text>
<rect x="370" y="60" width="150" height="70" rx="14" fill="#111a3a" stroke="#00e5ff"/><text x="445" y="92">Claude Code</text><text x="445" y="112" font-size="13" fill="#9aa7d6">думает и делает</text>
<rect x="370" y="170" width="150" height="70" rx="14" fill="#111a3a" stroke="#00e5ff"/><text x="445" y="202">Папка проекта</text><text x="445" y="222" font-size="13" fill="#9aa7d6">файлы и результат</text>
<rect x="180" y="170" width="150" height="70" rx="14" fill="#111a3a" stroke="#ff4fd8"/><text x="255" y="202">Защита</text><text x="255" y="222" font-size="13" fill="#9aa7d6">ключи, ufw, fail2ban</text>
<text x="256" y="292" fill="#9aa7d6" font-size="13">ответ возвращается в чат</text></g>
<g stroke="#00e5ff" stroke-width="2.5" fill="none" marker-end="url(#a)">
<path d="M124 150 C150 120 160 100 178 95"/><path d="M330 95 L368 95"/><path d="M445 130 L445 168"/><path d="M445 242 L445 268 L66 268 L66 202" stroke-dasharray="5 5"/></g></svg>"""


def build_home():
    h = HOME
    cards = "".join(f'<div class="card">{E(x)}</div>' for x in h["who"])
    steps = "".join(
        f'<a class="card step" href="steps/{n:02d}.html"><div class="n">{n}</div><h3>{E(s["t"])}</h3><p>{E(s["short"])}</p><span class="go">Открыть шаг →</span></a>'
        for n, s in enumerate(STEPS, 1))
    return (head("ИИ-сервер за вечер — свой Claude Code на сервере и в Telegram", "Пошаговая инструкция для новичков: арендуй сервер, установи Claude Code, подключи Telegram-бота и управляй ИИ с телефона.", 0)
    + top(0) + f"""<main class="wrap">
<section class="hero"><div><h1><span>{E(h['h1'])}</span></h1><p class="lead">{E(h['sub'])}</p>
<div class="actions"><a class="btn" href="steps/01.html">Начать с шага 1</a><a class="btn ghost" href="example.html">Как это у нас</a></div></div>
<div class="byte"><div class="bubble">{E(h['byte'])}</div><img src="img/byte-happy.webp" alt="Робот БАЙТ" width="330" height="324"></div></section>
<section class="who"><h2>Кому подходит</h2><div class="grid3">{cards}</div></section>
<section id="steps"><h2>7 шагов</h2><p class="sub">Каждый шаг открывается отдельной страницей: команды, что должно получиться и частые ошибки.</p><div class="steps">{steps}</div></section>
<section class="live"><div><h2>Живой пример: наш сервер</h2><p>{E(h['live'])}</p><p><a class="btn small ghost" href="example.html">Посмотреть, как всё устроено</a></p></div><div>{diagram()}</div></section>
<section id="nq" class="box nq"><h2>Научись говорить с ИИ — через игру</h2><p>Сервер и бот — это инструменты. Чтобы получать от ИИ нужный результат, нужно уметь ставить задачи. В бесплатной игре НЕЙРОКВЕСТ ты тренируешь это вместе с роботом БАЙТом.</p>
<div class="links"><a class="btn" href="{GAME}" rel="noopener">▶ Играть бесплатно</a><a class="btn ghost" href="{APK}" rel="noopener">📱 Скачать APK</a><a class="btn ghost" href="{TG}" rel="noopener">🤖 Telegram</a><a class="btn ghost" href="{GH}" rel="noopener">💻 GitHub</a></div></section>
</main>""" + foot(0))


def build_step(n):
    s = STEPS[n - 1]
    prev = f'<a class="btn ghost" href="{n-1:02d}.html">← Шаг {n-1}</a>' if n > 1 else '<a class="btn ghost" href="../index.html">← На главную</a>'
    nt = STEPS[n]["t"] if n < 7 else ""
    nxt = f'<a class="btn" href="{n+1:02d}.html">Шаг {n+1}: {E(nt)} →</a>' if n < 7 else '<a class="btn" href="../index.html">🎉 Готово — на главную</a>'
    errs = "".join(f"<li>{E(x)}</li>" for x in s["errs"])
    return (head(f"Шаг {n}. {s['t']} — ИИ-сервер за вечер", s["short"], 1) + top(1) + f"""<main class="wrap page">
<div class="crumb"><a href="../index.html">Главная</a> → Шаг {n} из 7</div><div class="bar"><i style="width:{round(n/7*100)}%"></i></div>
<h1>{n}. {E(s['t'])}</h1>
<div class="guide"><img src="../img/byte-happy.webp" alt="БАЙТ" width="76" height="75"><div class="bubble">{E(s['byte'])}</div></div>
<h2>Зачем это нужно</h2><p>{E(s['why'])}</p>
{body(n)}
<h2>Что должно получиться</h2><div class="what">{E(s['got'])}</div>
<h2>Частые ошибки</h2><div class="err"><ul>{errs}</ul></div>
<div class="pn">{prev}{nxt}</div></main>""" + foot(1))


def build_example():
    return (head("Живой пример: как устроен наш сервер — ИИ-сервер за вечер", "Как у автора сайта организованы сервер, Telegram-боты и Claude Code: схема без секретов.", 0)
    + top(0) + f"""<main class="wrap page"><div class="crumb"><a href="index.html">Главная</a> → Живой пример</div>
<h1>Как устроен наш сервер</h1>
<div class="guide"><img src="img/byte-happy.webp" alt="БАЙТ" width="76" height="75"><div class="bubble">Всё то же самое, что ты соберёшь по шагам, — только в большем масштабе! 🤖</div></div>
<p>{E(HOME['live'])}</p>
<div style="max-width:620px;margin:20px auto">{diagram()}</div>
<h2>Из чего это состоит</h2>
<ul><li><b>Сервер на Ubuntu</b> — обычный виртуальный сервер, который работает круглосуточно.</li>
<li><b>Несколько Telegram-ботов-помощников.</b> Каждый — отдельная служба systemd со своей задачей: тексты, программирование, финансовая аналитика, работа с заказами. Один бот — одна папка и один набор правил.</li>
<li><b>Claude Code на сервере</b> — «мозг» каждого помощника. Бот передаёт ему задачу и возвращает ответ в чат.</li>
<li><b>Удалённый доступ к сессиям</b> — отдельная служба позволяет открывать рабочие сессии Claude Code с телефона.</li>
<li><b>Защита</b>: вход по SSH-ключам, сетевой экран, fail2ban, секреты в отдельных файлах, а не в коде.</li>
<li><b>Рабочий стол и браузер</b> на сервере — для задач, которые нужно делать через сайты. Это уже следующий уровень, он не нужен для старта.</li></ul>
<div class="note">Мы специально не показываем адреса, имена пользователей, токены и идентификаторы. На твоём сервере всё это будет твоим личным и закрытым.</div>
<h2>Что можно повторить уже сегодня</h2>
<p>Базовая версия — сервер, Claude Code, один бот и автозапуск — собирается за вечер по нашим шагам.</p>
<div class="partners"><a class="btn" href="steps/01.html">Начать с шага 1</a><a class="btn ghost" href="{TG}" rel="noopener">Задать вопрос в сообществе</a></div></main>""" + foot(0))


(ROOT / "index.html").write_text(build_home(), encoding="utf-8")
(ROOT / "example.html").write_text(build_example(), encoding="utf-8")
for n in range(1, 8):
    (ROOT / "steps" / f"{n:02d}.html").write_text(build_step(n), encoding="utf-8")
(ROOT / ".nojekyll").write_text("")
print("built")
