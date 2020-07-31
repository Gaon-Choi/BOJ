#include <string>
#include <iostream>
#include <vector>


int gcd(long long a, long long b) {
	while (b != 0) {
		long long r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int lcm(long long a, long long b) {
	return a * b / gcd(a, b);
}

int main(void) {
	int cnt;
	std::cin >> cnt;

	long long a, b;
	std::vector<long long> vec;

	for (int i = 0; i < cnt; i++) {
		std::cin >> a >> b;
		vec.push_back(lcm(a, b));
	}

	for (int i = 0; i < cnt; i++) {
		std::cout << vec[i] << std::endl;
	}
	
	return 0;
}