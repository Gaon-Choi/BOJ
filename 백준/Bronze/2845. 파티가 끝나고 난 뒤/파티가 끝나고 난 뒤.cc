#include <iostream>
#include <vector>

int main(void) {
	int num, area;
	std::cin >> num >> area;
	std::vector<int> vec(5);
	for (size_t i = 0; i < vec.size(); i++)
		std::cin >> vec[i];
	for (size_t i = 0; i < vec.size(); i++)
		std::cout << vec[i] - (num * area) << " ";
	return 0;
}