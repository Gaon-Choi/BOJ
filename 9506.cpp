#include <vector>
#include <iostream>

void test_number(int num) {
	int sum = 0;
	std::vector<int> vec2;
	for (int i = 1; i < num; ++i) {
		if (num % i == 0) {
			vec2.emplace_back(i);
			sum += i;
		}
	}
	if (sum != num)
		std::cout << num << " is NOT perfect." << std::endl;
	else {
		std::cout << num << " = ";
		for (int i = 0; i < vec2.size() - 1; ++i)
			std::cout << vec2[i] << " + ";
		std::cout << vec2[vec2.size() - 1] << std::endl;
	}
}

int main() {
	int n;
	std::vector<int> vec;
	while (true) {
		std::cin >> n;
		if (n != -1) vec.emplace_back(n);
		else break;
	}
	for (int i = 0; i < vec.size(); ++i)
		test_number(vec[i]);
	return 0;
}