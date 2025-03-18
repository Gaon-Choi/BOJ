#include <iostream>
#include <vector>

int main(void) {
	int n;
	std::cin >> n;
	std::vector<double> vec(n);
	for (int i = 0; i < vec.size(); i++) {
		double j;
		std::cin >> j;
		vec[i] = 0.8 * j;
	}
	for (int i = 0; i < vec.size(); i++)
		printf("$%.2f\n", vec[i]);
	return 0;
}