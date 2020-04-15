#include <iostream>
#include <vector>

int main(void) {
	int num;
	std::cin >> num;
	std::vector<int> vec;
	int a, b;
	for (int i = 0; i < num; i++) {
		std::cin >> a >> b;
		vec.emplace_back(a + b);
	}
	for (int i = 0; i < num; i++)
		std::cout << "Case #" << (i + 1) << ": " << vec[i] << std::endl;
	return 0;
}