#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main() {
	int X, N, a, b;
	int total = 0;
	std::cin >> X >> N;
	for (int i = 0; i < N; i++) {
		std::cin >> a >> b;
		total += a * b;
	}
	if (total == X)
		std::cout << "Yes";
	else
		std::cout << "No";

	return 0;
}