#include <iostream>
#include <string>
#include <vector>

int get_distance(std::string str1, std::string str2) {
	int distance = 0;
	for (int i = 0; i < str1.size(); i++) {
		if (str1[i] != str2[i])
			distance++;
	}
	return distance;
}

int main(void) {
	int count;
	std::string str1, str2;
	std::cin >> count;

	std::vector<int> vec;

	for (int i = 0; i < count; i++) {
		std::cin >> str1;
		std::cin >> str2;
		vec.push_back(get_distance(str1, str2));
	}

	for (int i = 0; i < count; i++)
		std::cout << "Hamming distance is " << vec[i] << "." << std::endl;
	return 0;
}