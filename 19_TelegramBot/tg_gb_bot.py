# pip install telebot
# pip install PyTelegramBotAPI==2.2.3
# pip install PyTelegramBotAPI==3.6.7
import telebot
from random import *
import json
from os import system

system('cls')

films =[]

def save():
	with open('19_TelegramBot/films.json', 'w', encoding = 'UTF-8') as fh:
		fh.write(json.dumps(films, ensure_ascii = False))
	print('Наша фильмотека была успешно сохранена в файле films.json')

def load():
	global films
	with open('19_TelegramBot/films.json', 'r', encoding = 'UTF-8') as fh:
		films = json.load(fh)
	print("Фильмотека была успешно загружена")

API_TOKEN = '5762531742:AAH5Ujt0YuiosA0pc-8KSWGXsn-albbw390'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_message(message):
	try:
		load()
		bot.send_message(message.chat.id, 'Фильмотека была успешно загружена!')
	except:
		films.append("Матрица")
		films.append("Солярис")
		films.append("Властелин колец")
		films.append("Техасская резня бензопилой")
		films.append("Санта Барбара")
		bot.send_message(message.chat.id, 'Фильмотека была загружена по умолчанию!')

@bot.message_handler(commands = ['all'])
def show_all(message):
	bot.send_message(message.chat.id, 'Вот список фильмов')
	bot.send_message(message.chat.id, ', '.join(films))

bot.polling()