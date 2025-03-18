#include <iostream>
#include <string>
int main(void) {
	int len;
	int x = 0, y = 0;
	std::cin >> len;
	std::string str;
	std::cin >> str;
	for (int i = 0; i < len; i++) {
		if (str[i] == '2') x++;
		if (str[i] == 'e') y++;
	}
	if (x > y)
		std::cout << "2";
	else if (x == y)
		std::cout << "yee";
	else
		std::cout << "e";
	return 0;
}