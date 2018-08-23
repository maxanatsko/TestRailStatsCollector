import datetime
import telegram
from sources.config_reader import config as cr

# Get data from config file
bot_token = cr.get('Telegram', 'bot_token')
chat_id = cr.get('Telegram', 'chat_id')

bot = telegram.Bot(token=bot_token)

def send_telegram_message(msg_text):
    bot.send_message(chat_id=chat_id, text="*{:%Y-%m-%d %H:%M}:* `{}`".format(datetime.datetime.now(), msg_text),parse_mode=telegram.ParseMode.MARKDOWN)