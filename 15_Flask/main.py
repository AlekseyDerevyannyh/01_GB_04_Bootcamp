# pip install flask
from os import system
from flask import Flask		# Вытащил объект 

system("cls")

app = Flask(__name__)		# Создали веб приложение

@app.route('/<x>/<y>')		# Создание главной страницы
def main(x, y):
	return str(int(x) + int(y))

if __name__ == '__main__':
	app.run()