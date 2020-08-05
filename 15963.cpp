#include <iostream>
#include <string>

int main(void) {
	std::string s1, s2;
	std::cin >> s1 >> s2;

	if (s1 == s2)
		std::cout << 1;
	else
		std::cout << 0;
	return 0;
}