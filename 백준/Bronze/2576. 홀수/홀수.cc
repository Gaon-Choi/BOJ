#include <iostream>
#include <limits.h>

int main(void) {
	int num;
	int min = INT_MAX;
	int sum = 0;
	for(int i = 0; i < 7;i++){
		std::cin >> num;
		if (num % 2 == 1) {
			sum += num;
			if (min > num)
				min = num;
		}
	}
	if (sum == 0)
		std::cout << -1;
	else
		std::cout << sum << "\n" << min;
	return 0;
}