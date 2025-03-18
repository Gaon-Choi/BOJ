#include <string>
#include <vector>
#include <iostream>
using namespace std;

int main() {
	int A, B;

	std::cin >> A >> B;

	std::vector<int> arr;
	int i = 1;
	while (arr.size() <= 1000) {
		for (int j = 1; j <= i; j++)
			arr.push_back(i);
		i++;
	}

	int result = 0;
	for (int idx = A - 1; idx < B; idx++)
		result += arr.at(idx);

	std::cout << result;
	return 0;
}