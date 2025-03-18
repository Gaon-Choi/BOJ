#include <iostream>

int a[4];

int main() {
	std::cin >> a[0] >> a[1] >> a[2] >> a[3];
	std::cout << a[0] * a[1] + a[2] * a[3];
	return 0;
}