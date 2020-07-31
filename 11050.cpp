#include <iostream>

int factorial(int n) {
	if (n == 0 || n == 1)
		return 1;
	else
		return n * factorial(n - 1);
}

int main(void) {
	int n, k;
	std::cin >> n >> k;
	std::cout << factorial(n) / (factorial(k) * factorial(n - k));
	return 0;
}