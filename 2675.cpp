#include <iostream>
#include <string>
#include <vector>

int main(void) {
	int count;
	std::cin >> count;
	std::vector<std::string> vec;

	int m, i;
	std::string str;

	for (i = 0; i < count; i++) {
		std::string s;
		std::cin >> m >> str;
		for (int j = 0; j < str.size(); j++) {
			for (int k = 0; k < m; k++)
				s += str[j];
		}
		vec.push_back(s);
	}

	for (i = 0; i < count; i++)
		std::cout << vec[i] << std::endl;

	return 0;
}