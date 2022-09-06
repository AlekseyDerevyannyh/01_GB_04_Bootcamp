// Сортировка массива строк методом выбора

using System;
using static System.Console;

Clear();

string[] array = new string[5];
for (int i = 0; i < 5; i++) {
	array[i] = ReadLine();
}

Write("[" + string.Join(", ", array) + "]");
for (int i = 0; i < 4; i++) {
	int MinIndex = i;
	for (int j = i + 1; j < 5; j++) {
		if (array[j].Length < array[MinIndex].Length)	MinIndex = j; 
	}
	string temp;
	temp = array[MinIndex];
	array[MinIndex] = array[i];
	array[i] = temp;
}
WriteLine("Конечный массив: [" + string.Join(", ", array) + "]");