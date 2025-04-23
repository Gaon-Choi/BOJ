#include <iostream>
using namespace std;

int n;
bool prime_[4000001];
int arr[2000001], l, r, ret, sum, p;

int main() {
	cin >> n;

	for (int i = 2; i <= n; ++i) {
		if (prime_[i])	continue;

		for (int j = 2 * i; j <= n; j += i) {
			prime_[j] = true;
		}
	}

	for (int i = 2; i <= n; ++i) {
		if (!prime_[i]) {
			arr[p] = i;
			p++;
		}
	}

	while (true) {
		if (sum == n)
			ret++;

		if (sum >= n) {
			sum -= arr[l++];
		}
		else if (r == p)
			break;
		//else if (n <= sum)
		else {
			sum += arr[r++];
		}
	}

	cout << ret;

	return 0;
}