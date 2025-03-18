#include <iostream>

int main(void) {
	int a, b, c, d;
	std::cin >> a >> b >> c >> d;
	int sum = a + b + c + d;
	std::cout << int(sum / 60) << "\n" << sum % 60;
	return 0;
}