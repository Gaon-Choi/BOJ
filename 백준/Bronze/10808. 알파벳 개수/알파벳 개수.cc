#include <iostream>
#include <string>

int main(void) {
	int arr[26] = { 0, };
	std::string str;
	std::cin >> str;
	for (int i = 0; i < str.length(); i++) {
		arr[(int)(str[i]) - 97] += 1;
	}
	for (int i = 0; i < 26; i++)
		std::cout << arr[i] << " ";
	return 0;
}