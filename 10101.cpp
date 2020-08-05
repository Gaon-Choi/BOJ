#include <iostream>

int main(void) {
	int a1, a2, a3;
	std::cin >> a1 >> a2 >> a3;

	if (a1 + a2 + a3 != 180)
		std::cout << "Error";
	else {
		bool b1 = (a1 == a2);
		bool b2 = (a2 == a3);
		bool b3 = (a3 == a1);
		int sum = b1 + b2 + b3;
		if (sum == 0)
			std::cout << "Scalene";
		else if (sum == 1)
			std::cout << "Isosceles";
		else
			std::cout << "Equilateral";
	}
	return 0;
}