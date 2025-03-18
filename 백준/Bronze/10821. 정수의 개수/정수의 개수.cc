#include <iostream>
#include <string>

int main(void) {
	std::string str;
	std::cin >> str;
	int i = 0, s = 0;
	while (true) {
		if (str[i]=='\0')
			break;
		if (str[i]==',')
			s++;
		i++;
	}
	std::cout << s + 1;
	return 0;
}