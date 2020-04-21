#include <iostream>
#include <vector>
#include <algorithm>

int main(void) {
	int size;
	std::cin >> size;
	std::vector<int> a(size);
	std::vector<int> b(size);
	for (int i = 0; i < size; i++)std::cin >> a[i];
	for (int i = 0; i < size; i++)std::cin >> b[i];
	std::sort(a.begin(), a.end(), std::greater<int>());
	std::sort(b.begin(), b.end(), std::less<int>());
	int sum = 0;
	for (int i = 0; i < size; i++) sum += a[i] * b[i];
	std::cout << sum;
	return 0;
}