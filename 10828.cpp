#include <iostream>
#include <stack>
#include <string>
#include <vector>

int main(void) {
	// empty stack
	std::stack<int> s;
	
	// a vector that includes results after each commands
	std::vector<int> vec;

	// the number of commands
	int count;
	std::cin >> count;
	int element; // in case of insertion

	// menu
	std::string str;

	int i;
	for (i = 0; i < count; i++) {
		std::cin >> str;
		if (str == "push") {
			std::cin >> element;
			s.push(element);
		}
		else if (str == "top") {
			if (s.empty())
				vec.push_back(-1);
			else
				vec.push_back(s.top());
		}
		else if (str == "pop") {
			if (s.empty())
				vec.push_back(-1);
			else {
				vec.push_back(s.top());
				s.pop();
			}
		}
		else if (str == "size")
			vec.push_back(s.size());
		else
			vec.push_back(s.empty());
	}

	for (i = 0; i < vec.size(); i++)
		std::cout << vec[i] << std::endl;

	return 0;
}