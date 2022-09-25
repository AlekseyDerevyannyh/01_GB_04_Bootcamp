# pip install flask
# pip install flask-wtf
# pip install email_validator

from os import system
from flask import Flask, render_template	# Вытащил объект 
from auth import LoginForm

system("cls")

app = Flask(__name__)	# Создали веб приложение
app.config['SECRET_KEY'] = 'world world world hello'	#csrf атаки

@app.route('/', methods=['GET', 'POST'])	# Создание главной страницы
def main():
	form = LoginForm()
	if form.validate_on_submit():
		name = form.name.data
		surname = form.surname.data
		email = form.email.data
		print(name, surname, email)
		return render_template('base.html', title = 'Главная страница', message = 'Вы авторизовались')
	return render_template('base.html', title = 'Главная страница', form = form)

if __name__ == '__main__':
	app.run()
