#include <iostream>

int main() {
	int num;
	std::cin >> num;
	/*
	if (num == 1) {
		std::cout << 1;
		exit(0);
	}
	*/
	while (num != 1) {
		int i = 2;
		while (num % i != 0) i++;
		num /= i;
		std::cout << i << "\n";
	}
	return 0;
}