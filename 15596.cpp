#include <iostream>

long long sum(int* a, int n) {
	long long total = 0;
	long long num;
	for (int i = 0; i < n; i++)
		total += *(a + i);
	return total;
}