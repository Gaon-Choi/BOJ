#include <iostream>
#include <set>

int main() {
	std::set<int> s;
	int a, b;
	int data;
	std::cin >> a >> b;
	for (int i = 0; i < a; ++i) std::cin >> data, s.insert(data);
	for (int i = 0; i < b; ++i) std::cin >> data, s.insert(data);
	std::cout << a + b - 2 * (a + b - s.size());
	return 0;
}