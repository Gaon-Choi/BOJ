#include <iostream>

int a[6];

int main() {
	std::cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4] >> a[5];
	std::cout << 1 - a[0] << " " << 1 - a[1] << " " << 2 - a[2] << " "
		<< 2 - a[3] << " " << 2 - a[4] << " " << 8 - a[5];
	return 0;
}