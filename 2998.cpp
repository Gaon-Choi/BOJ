#include <iostream>
#include <string>

int main(void) {
	std::string str;
	std::cin >> str;
	while (str.length() % 3 != 0)
		str = "0" + str;
	int length = str.length() / 3;
	int number = atoi(str.c_str());
	for (int i = 0; i < length; i++)
		std::cout << atoi(str.substr(3 * i, 1).c_str()) * 4
		+ atoi(str.substr(3 * i + 1, 1).c_str()) * 2
		+ atoi(str.substr(3 * i + 2, 1).c_str());
	return 0;
}