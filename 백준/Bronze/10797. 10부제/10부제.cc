#include <iostream>

int main(void) {
	int a;
	std::cin >> a;
	int s = 0;
	for (int i = 0; i < 5; i++) {
		int b;
		std::cin >> b;
		if (a == b)s++;
	}
	std::cout << s;
	return 0;
}