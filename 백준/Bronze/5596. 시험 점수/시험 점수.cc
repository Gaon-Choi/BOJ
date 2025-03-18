#include <iostream>
#include <algorithm>

int main(void) {
	int minkuk = 0, manse = 0;
	int a, i;
	for (i = 0; i < 4; i++) {
		std::cin >> a;
		minkuk += a;
	}
	for (i = 0; i < 4; i++) {
		std::cin >> a;
		manse += a;
	}
	std::cout << std::max(minkuk, manse);
	return 0;
}