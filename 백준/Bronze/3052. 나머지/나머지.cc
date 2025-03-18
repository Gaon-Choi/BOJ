#include <iostream>
#include <set>
int main(void) {
	std::set<int> set;
	for (int i = 0; i < 10; i++) {
		int a;
		std::cin >> a;
		set.emplace(a % 42);
	}
	std::cout << set.size();
	return 0;
}