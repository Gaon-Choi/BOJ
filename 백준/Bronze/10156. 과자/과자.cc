#include <iostream>

int K, N, M;

int main() {
	std::cin >> K >> N >> M;
	int m = K * N - M;
	if (m >= 0) std::cout << m;
	else std::cout << 0;
	return 0;
}