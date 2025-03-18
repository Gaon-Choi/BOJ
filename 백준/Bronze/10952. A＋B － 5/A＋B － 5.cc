#include <iostream>
#include <vector>

int main() {
	int a, b;
	std::vector<int> vec;
	while (true) {
		std::cin >> a >> b;
		if (a == '\0' && b == '\0')
			break;
		vec.emplace_back(a + b);
	}
	for (int i = 0; i < vec.size(); i++)
		std::cout << vec[i] << std::endl;
	return 0;
}