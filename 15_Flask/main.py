# pip install flask
from os import system
from flask import Flask, render_template	# Вытащил объект 

system("cls")

app = Flask(__name__)	# Создали веб приложение

@app.route('/<name>')	# Создание главной страницы
def main(name):
	title = 'Igor'
	return render_template('base.html', name = name, title = 'BootCamp')

if __name__ == '__main__':
	app.run()