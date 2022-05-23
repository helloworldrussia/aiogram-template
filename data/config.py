from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

user = env.str("user")
password = env.str("password")


admin1 = env.str("admin1")
admin2 = env.str("admin2")

start_text = '''Я – бот «Бумажное сердце», и я рад вас видеть.

В этом месяце я буду помогать вам быть на связи с собой – присылать сообщения в разные моменты дня, чтобы вы сделали быстрый чек-ин.

📍А ещё я умею собирать вопросы для Стаса.

Чтобы отправить вопрос, нажмите на кнопку «Вопрос Стасу», и у нас всё получится.

Если у вас не высвечивается кнопка для отправки запроса, нажмите на значок «🎛» в правом нижнем углу экрана.'''
