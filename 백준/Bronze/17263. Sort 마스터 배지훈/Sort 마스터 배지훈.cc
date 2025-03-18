#include <iostream>
#include <string>

int main(void) {
	int num;
	std::cin >> num;
	int max_num = -1;
	int a;
	for (int i = 0; i < num; i++) {
		std::cin >> a;
		if (max_num < a)
			max_num = a;
	}
	std::cout << max_num;
	return 0;
}