#include <iostream>
#include <algorithm>
#include <vector>

long long x[4], y[4], s[6];

int main(void) {
	int i, j, k, tc;
	std::cin >> tc;
	std::vector<int> vec(tc);
	for (int p = 0; p < tc; p++) {
		k = 0;
		for (i = 0; i < 4; i++)
			std::cin >> x[i] >> y[i];

		for (i = 0; i < 4; i++)
			for (j = i + 1; j < 4; j++) {
				s[k] = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]);
				k++;
			}
		std::sort(s, s + 6);
		vec[p] = (s[0] == s[1]) && (s[1] == s[2]) && (s[2] == s[3]) && (s[4] == s[5]);
	}
	for (int p = 0; p < vec.size(); p++)
		std::cout << vec[p] << '\n';
	return 0;
}