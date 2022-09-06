# основы ООП на примере гонки черепах

from turtle import *
from random import randint
from time import *

screen = Screen()

finish = 200		# дистанция гонки

t1 = Turtle()		# создали объект класса черепахи
t1.shape("turtle")	# поменяли форму объекта
t1.color("red")		# поменяли цвет объекта
t1.penup()			# поднимаем черепашку, чтоб не рисовала
t1.goto(-200,20)	# перемещаем черепашку по координатам
t1.pendown()		# опускаем черепашку, чтоб потом рисовала
t1.speed(3)

t2 = Turtle()		# создали объект класса черепахи
t2.shape("turtle")	# поменяли форму объекта
t2.color("blue")	# поменяли цвет объекта
t2.penup()			# поднимаем черепашку, чтоб не рисовала
t2.goto(-200, -20)	# перемещаем черепашку по координатам
t2.pendown()		# опускаем черепашку, чтоб потом рисовала
t2.speed(3)

def razmetka():		# функция рисует разметку поля
	t = Turtle()
	for i in range(1, 21):
		t.penup()
		t.goto(-200 + i * 20, 50)
		t.pendown()
		t.goto(-200 + i * 20, -100)
	t.hideturtle()

razmetka()

def catch1(x, y):		# обработчик события нажатия
	t1.write('Ouch!', font = ('Arial', 14, 'normal'))	# пишем на экране "Ауч"
	t1.fd(randint(10, 15))								# черепашка делает случайный шаг от 10 до 15

t1.onclick(catch1)		# прикрепляем обработчик события к нажатию на черепашку 1

def catch2(x, y):
	t2.write('Мне больно!', font = ('Arial', 14, 'normal'))
	t2.fd(randint(10, 15))

t2.onclick(catch2)		# прикрепляем обработчик события к нажатию на черепашку 1

while  t1.xcor() < finish and t2.xcor() < finish:	# запуск гонки
	t1.forward(randint(2, 7))
	t2.forward(randint(2, 7))
	sleep(0.05)

screen.exitonclick()