#include <iostream>

int main(void) {
	int d;
	std::cin >> d;
	int star = 2 * d - 1;
	int blank = 0;
	for (int i = 0; i < d; i++) {
		for (int k = 0; k < blank; k++)
			std::cout << " ";
		for (int j = 0; j < star; j++)
			std::cout << "*";
		std::cout << std::endl;
		star -= 2;
		blank += 1;
	}
	return 0;
}