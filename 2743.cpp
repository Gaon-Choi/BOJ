#include <iostream>
#include <cstring>

int main(void) {
	char* text = new char[100];
	std::cin >> text;
	std::cout << strlen(text);
	delete[] text;
	return 0;
}