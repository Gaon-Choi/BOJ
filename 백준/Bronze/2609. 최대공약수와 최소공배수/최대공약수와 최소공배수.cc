#include <iostream>
using namespace std;
int gcd(int a, int b) {
	while (b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int lcm(int a, int b) {
	return a * b / gcd(a, b);
}
int main(void) {
	int a, b;
	std::cin >> a >> b;
	std::cout << gcd(a, b) << "\n" << lcm(a, b);
	return 0;
}