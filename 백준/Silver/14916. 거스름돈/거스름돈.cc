#include <bits/stdc++.h>
using namespace std;

int dp[1000001];
int n;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;

	fill(dp, dp + 1000001, -1);

	dp[0] = 0;

	for (int i = 1; i <= n; ++i) {
		int res = INT_MAX;

		if (i - 2 >= 0 && dp[i - 2] != -1) {
			res = min(res, dp[i - 2] + 1);
		}

		if (i - 5 >= 0 && dp[i - 5] != -1) {
			res = min(res, dp[i - 5] + 1);
		}

		if (res != INT_MAX)
			dp[i] = res;
	}

	cout << dp[n];

	return 0;
}
