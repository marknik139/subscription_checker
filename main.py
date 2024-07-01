import os
from dotenv import load_dotenv
import telebot
from telebot import types

# Загрузка переменных из .env файла
load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_USERNAME = os.getenv('CHANNEL_USERNAME')
LINK = os.getenv('LINK')

bot = telebot.TeleBot(TOKEN)

def create_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_button = types.KeyboardButton('Получить ссылку')
    markup.add(start_button)
    return markup

def check_subscription_status(user_id):
    try:
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return True
    except telebot.apihelper.ApiException:
        pass
    return False

def send_subscription_message(chat_id, is_subscribed):
    markup = create_reply_keyboard()
    if is_subscribed:
        bot.send_message(chat_id, f'Спасибо за подписку! Вот ваша ссылка: {LINK}', reply_markup=markup)
    else:
        bot.send_message(chat_id, f'Подпишитесь на канал {CHANNEL_USERNAME}, чтобы получить ссылку.', reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    is_subscribed = check_subscription_status(user_id)
    send_subscription_message(message.chat.id, is_subscribed)

@bot.message_handler(func=lambda message: message.text == 'Получить ссылку')
def handle_aaa(message):
    start(message)

if __name__ == '__main__':
    bot.polling(none_stop=True)
