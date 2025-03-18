#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
	std::vector<int> result;
	int n;
	for (int i = 0; i < 5; i++) {
		std::cin >> n;
		result.push_back(n);
	}

	std::sort(result.begin(), result.end());

	std::cout << std::accumulate(result.begin(), result.end(), 0) / result.size() << std::endl;
	std::cout << result[2];

	return 0;
}