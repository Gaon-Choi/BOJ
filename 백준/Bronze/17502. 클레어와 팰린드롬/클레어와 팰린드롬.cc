#include <iostream>
#include <string>

int main(void) {
	int size;
	std::string str;
	std::cin >> size;
	std::cin >> str;
	for (int i = 0; i < size; i++) {
		if (str[i] == '?') {
			if (str.substr(size-i-1, 1) != "?") str[i] = str[size - i-1];
			else str[i] = str[size - i-1] = 'a';
		}
	}
	std::cout << str;
	return 0;
}