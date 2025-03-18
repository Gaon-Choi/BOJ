#include <iostream>
#include <vector>

int main(void) {
	int a, b, c;
	int case_num;
	std::cin >> case_num;
	std::vector<int> vec(case_num);
	for (int i = 0; i < case_num; i++) {
		std::cin >> a >> b >> c;
		if (a > b - c)
			vec[i] = 0;
		if (a == b - c)
			vec[i] = 1;
		if (a < b - c)
			vec[i] = 2;
	}
	for (int i = 0; i < vec.size(); i++) {
		if (vec[i] == 0)
			std::cout << "do not advertise\n";
		if (vec[i] == 1)
			std::cout << "does not matter\n";
		if (vec[i] == 2)
			std::cout << "advertise\n";
	}
	return 0;
}