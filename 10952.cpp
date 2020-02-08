#include <iostream>
#include <vector>

int main(void) {
	int a, b;
	std::vector<int> vec;
	while (true) {
		std::cin >> a >> b;
		if (a == 0 && b == 0)
			break;
		else
			vec.emplace_back(a + b);
	}
	std::vector<int>::iterator iter;
	for (iter = vec.begin(); iter != vec.end(); iter++)
		std::cout << *iter << std::endl;
	return 0;
}