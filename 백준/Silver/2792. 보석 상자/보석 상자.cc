#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll n, m, result = 1e18;
ll arr[300001];

bool search(ll estimate_val) {
	ll ret = 0;

	for (ll i = 0; i < m; ++i) {
		ret += arr[i] / estimate_val;
		if (arr[i] % estimate_val) ret++;
	}

	return ret <= n;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	ll left = 1, right = 0, mid;

	for (ll i = 0; i < m; ++i) {
		cin >> arr[i];
		right = max(right, arr[i]);
	}

	while (left <= right) {
		mid = (left + right) / 2;

		if (search(mid)) {
			result = min(result, mid);
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}

	cout << result;

	return 0;
}