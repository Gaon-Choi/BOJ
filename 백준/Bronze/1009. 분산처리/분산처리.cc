#include <iostream>
#include <vector>

long long pow_modular(long long base, int index, int mod = 10) {
	long long r = 1;
	while (index != 0) {
		if (index & 1)
			r = (r * base) % mod;
		base = (base * base) % mod;
		index >>= 1;
	}
	return r;
}

int main(void) {
	int size, i;
	std::cin >> size;
	std::vector<int> a(size);
	std::vector<int> b(size);
	std::vector<int> ans(size);
	for (i = 0; i < size; i++) {
		std::cin >> a[i] >> b[i];
		ans[i] = pow_modular(a[i], b[i]);
	}
	for (i = 0; i < size; i++) {
		if (ans[i] == 0)
			std::cout << 10 << std::endl;
		else
			std::cout << ans[i] << std::endl;
	}
	return 0;
}