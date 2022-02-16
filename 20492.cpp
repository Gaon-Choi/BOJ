#include <iostream>

int main() {
	long long s;
	std::cin >> s;
	std::cout << (int)(0.78 * s) << " " << (int)((0.8 * s) + (0.2 * s * 0.78));
	return 0;
}