#define INT_MAX 2147483647
#include <iostream>

int main(void) {
	int burger[3];
	int beverage[2];
	int min_1=INT_MAX, min_2=INT_MAX;
	int i = 0;
	for (i = 0; i <= 2; i++) {
		std::cin >> burger[i];
		if (min_1 > burger[i])
			min_1 = burger[i];
	}
	for (i = 0; i <= 1; i++) {
		std::cin >> beverage[i];
		if (min_2 > beverage[i])
			min_2 = beverage[i];
	}
	std::cout << (min_1 + min_2)-50;
	return 0;
}