#include <bits/stdc++.h>
using namespace std;

bool is_prime[1001];
int n, k;

int main() {
	fill(is_prime, is_prime + 1001, true);

	int cnt = 0;

	cin >> n >> k;

	for (int i = 2; i <= n; ++i) {
		for (int j = i; j <= n; j += i) {
			if (is_prime[j]) {
				is_prime[j] = false;
				cnt++;

				if (cnt == k) {
					cout << j;
					return 0;
				}
			}
		}
	}

	return 0;
}