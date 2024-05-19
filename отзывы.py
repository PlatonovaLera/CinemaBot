import telebot
import sqlite3
bot = telebot.TeleBot('6969036206:AAFrWpg8FYYCxUr8rTtOq_YmzajlM4n6WJU')

@bot.message_handler(commands=['start'])
def start(message):
    connect = sqlite3.connect('feedback.sql')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS feedback(id INTEGER auto_ibcrement primary key, name varchar(50), feedback varchar(50),""")
    connect.commit()
    cursor.close()
    connect.close() 

    bot.send_message(message.chat.id,'Пожалуйста, оставь свой отзыв=)')
    bot.send_message(message.chat.id,'Для начала введи свое имя')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    name = message.text.strip()
    bot.send_message(message.chat.id,'Для начала введи свое имя')
    bot.register_next_step_handler(message, user_feedback)
     
def user_feedback(message):
    feedback = message.text.strip()
     


bot.polling(non_stop=True)

