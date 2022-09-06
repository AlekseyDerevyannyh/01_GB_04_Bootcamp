# pip install flask
from os import system
from flask import Flask, render_template	# Вытащил объект 

system("cls")

app = Flask(__name__)	# Создали веб приложение

@app.route('/')	# Создание главной страницы
def main():
	user_name = ['Aleksey', 'Alla', 'Almir', 'Diana', 'Ilali']
	return render_template('base.html', user_name = user_name, title = 'BootCamp')

if __name__ == '__main__':
	app.run()