#include <iostream>
#include <string>

int main(void) {
	std::string str;
	std::cin >> str;
	for (int i = 97; i < 97 + 26; i++) {
		int a = -1, b = 0;
		while (b < str.length()) {
			if (str[b] == char(i)) {
				a = b;
				break;
			} b += 1;
		}
		std::cout << a << " ";
	}
}