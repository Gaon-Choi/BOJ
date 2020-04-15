#include <iostream>
#include <cmath>

int main(void) {
	int A, B, C;
	// A: fixed cost
	// B: variable cost
	// C: gross income
	std::cin >> A >> B >> C;

	if (B >= C)
		std::cout << -1;
	else {
		// solving the equation A+B*x = C*x
		// x : the number of products
		int point = ceil(A / (C - B)) + 1;
		std::cout << point;
	}
	return 0;
}