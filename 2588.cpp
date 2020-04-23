#include <iostream>

int main(void) {
	int a;
	std::cin >> a;
	int b;
	std::cin >> b;
	int x = (b / 100);
	int y = (b / 10) % (10 * x);
	int z = b - 100 * x - 10 * y;
	std::cout << a * z << "\n" << a * y << "\n" << a * x << "\n" << a * b;
	return 0;
}