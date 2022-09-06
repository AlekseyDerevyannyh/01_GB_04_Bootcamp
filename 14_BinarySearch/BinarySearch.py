from random import randint
from os import system

system("cls")

x = randint(0, 100)

count_perebor = 0
# метод последовательного перебора
for i in range(0, 101):
	count_perebor += 1
	if i == x:
		print("Число найдено!")
		break

print("Загаданное число было", x, " и для его поиска перебором потребовалось ", count_perebor, " итераций")

count_random = 1
# метод случайного отгадывания
y = randint(0, 100)
while x != y:
	y = randint(0, 100)
	count_random += 1

print("Загаданное число было", x, " и для его поиска угадыванием потребовалось ", count_random, " итераций")

# метод ручного бинарного поиска
# count_bin = 0
# print("Давай начнём игру - угадай число от 0 до 100")
# y = int(input("Введите число"))
# while x != y:
# 	if x < y:	print("меньше")
# 	else:		print("больше")
# 	y = int(input("Введите число"))
# 	count_bin += 1

# print("Загаданное число было", x, " и для его бинарного поиска потребовалось ", count_bin, " итераций")

# метод автоматического бинарного поиска
count_bin = 1
left_border = 0
right_border = 100
y = (left_border + right_border) // 2
while x != y:
	if x < y:	right_border = y - 1
	else:		left_border = y + 1
	y = (left_border + right_border ) // 2
	count_bin += 1

print("Загаданное число было", x, " и для его бинарного поиска потребовалось ", count_bin, " итераций")
