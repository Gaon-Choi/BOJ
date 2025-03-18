#include <iostream>

int main(void) {
	int sum, price;
	std::cin >> sum;
	for (int i = 0; i < 9; i++) {
		std::cin >> price;
		sum -= price;
	}
	std::cout << sum;
	return 0;
}