#include <bits/stdc++.h>
using namespace std;

int n, x, arr[1000001], s, e, sum, ans;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	s = 0, e = n - 1;

	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}

	cin >> x;

	sort(arr, arr + n);

	while (s < e) {
		sum = arr[s] + arr[e];

		if (sum == x)
			ans++;

		if (sum >= x) {
			e--;
		}
		else {
			s++;
		}
	}

	cout << ans;

	return 0;
}