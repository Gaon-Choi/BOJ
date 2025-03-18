#include <iostream>
#include <cmath>

int main(void) {
	int A, B, C;
	std::cin >> A >> B >> C;

	if (B >= C)
		std::cout << "-1" << std::endl;
	else {
		int point = ceil(A / (C - B)) + 1;
		std::cout << point << std::endl;
	}
	return 0;
}