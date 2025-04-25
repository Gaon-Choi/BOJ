#include <bits/stdc++.h>
using namespace std;

int n, total, coin;
long long arr[10001];
vector<int> coins;

int main() {
	cin >> n >> total;

	arr[0] = 1;

	for (int i = 0; i < n; ++i) {
		cin >> coin;
		coins.push_back(coin);

		for (int j = coin; j <= total; ++j) {
			arr[j] += arr[j - coin];
		}
	}

	cout << arr[total];

	return 0;
}