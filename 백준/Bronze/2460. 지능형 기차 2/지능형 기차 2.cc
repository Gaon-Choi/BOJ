#include <iostream>
#include <algorithm>
#include <vector>

int main(void) {
	std::vector<int> vec;
	int a, b;
	int sum = 0;
	for (int i = 0; i < 10; i++) {
		std::cin >> a >> b;
		sum += (-a + b);
		vec.emplace_back(sum);
	}
	auto minmax = std::minmax_element(vec.begin(), vec.end());
	std::cout << *(minmax.second);
	return 0;
}