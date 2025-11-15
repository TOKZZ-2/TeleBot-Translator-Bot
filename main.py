import telebot
import requests
from easygoogletranslate import EasyGoogleTranslate

BOT_TOKEN = "TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = """
🤖 Привет! Я твой бот переводчик
✅ Могу автоматически определять язык и отправлять тебе перевод!
✅ Отправь мне текст, а я переведу его на русский!
✅ Перевожу с более чем 100 языков со всего мира!
✅ Перевожу благодаря Google Translate
        """
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text)
def translate(message):
    need_translate = message.text
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        translator = EasyGoogleTranslate(
            source_language='auto',
            target_language='ru',
            timeout=5
        )
        result = translator.translate(need_translate)
        bot.send_message(message.chat.id, result)
    except Exception as e:
        error_text = f"❌ Произошла ошибка при переводе: {str(e)}"
        bot.send_message(message.chat.id, error_text)

bot.infinity_polling()


