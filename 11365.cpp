#include <iostream>
#include <string>
#include <vector>

int main(void) {
	std::string sentence;
	std::vector<std::string> vec;
	while (true) {
		std::getline(std::cin, sentence);
		if (sentence == "END")
			break;
		std::string o = "";
		for (int i = sentence.length() - 1; i >= 0; i--)
			o += sentence[i];
		vec.push_back(o);
	}
	for (int i = 0; i < vec.size(); i++)
		std::cout << vec[i] << std::endl;
	return 0;
}