#include <iostream>
#include <string>

int main(void) {
	std::string str;
	std::cin >> str;

	bool b = true;

	for (int i = 0; i <= (int)(str.size() / 2); i++) {
		if (str[i] != str[str.size() - i - 1])
			b = false;
	}

	std::cout << b;
	return 0;
}