#include <iostream>
#include <vector>
int main(void) {
	std::vector<int> vec;
	for (int i = 0; i < 9; i++) {
		int a;
		std::cin >> a;
		vec.emplace_back(a);
	}
	int max=vec[0], index=0;
	for (int i = 0; i < 9; i++) {
		if (vec[i] > max) {
			max = vec[i];
			index = i;
		}
	}
	std::cout << max << "\n" << index + 1;
	return 0;
}