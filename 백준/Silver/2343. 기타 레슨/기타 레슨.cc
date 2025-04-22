#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll n, m, result = 1e19;
ll arr[100001];

bool search(ll estimate_val) {
	ll ret = 0;
	ll temp = 0;

	for (ll i = 0; i < n; ++i) {
		if (temp + arr[i] <= estimate_val) {
			temp += arr[i];
		}
		else {
			temp = arr[i];
			ret++;
		}
	}
    
    if (temp) ret++;

	return ret <= m;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	cin >> n >> m;

	ll left = 1, right = 0, mid;

	for (ll i = 0; i < n; ++i) {
		cin >> arr[i];
        left = max(left, arr[i]);
		right += arr[i];
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