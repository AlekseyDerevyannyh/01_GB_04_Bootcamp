// Сдвиг массива на k элементов вправо, при положительном k и влево при отрицательно k

using System;
using static System.Console;

Clear();

int n = Convert.ToInt32(Console.ReadLine());
int[] a = new int[n];
int[] b = new int[n];
for (int i = 0; i < n; i++) {
	a[i] = Convert.ToInt32(Console.ReadLine());
}
int k = Convert.ToInt32(Console.ReadLine());
k = k % n;
if (k > 0) {
	for (int i = 0; i <= k; i++)
		b[i] = a[n - k + i];
	for (int i = 0; i < n - k; i++)
		b[k + i] = a[i];
	for (int i = 0; i < n; i++)
		Write(b[i] + " ");
} else {
	k = -k;
	for (int i = 0; i < k; i++)
		b[n - k + i] = a[i];
	for (int i = 0; i < n - k; i++)
		b[i] = a[k + i];
	for (int i = 0; i < n; i++)
		Write(b[i] + " ");
}