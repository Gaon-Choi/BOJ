#include <bits/stdc++.h>
using namespace std;

const int INF = 987654321;
int n, dp[16][1 << 16], dist[16][16];

int tsp(int here, int visited) {
	// 모두 방문한 경우
	if (visited == (1 << n) - 1) {
		return dist[here][0] ? dist[here][0] : INF;
	}

	int &ret = dp[here][visited];
	if (ret != -1)	return ret;

	ret = INF;

	for (int i = 0; i < n; ++i) {
		// 방문한 경우에는 스킵
		if (visited & (1 << i))	continue;
		// 같은 도시인 경우 스킵
		if (dist[here][i] == 0)	continue;

		ret = min(ret, tsp(i, visited | (1 << i)) + dist[here][i]);
	}

	return ret;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> dist[i][j];
		}
	}

	memset(dp, -1, sizeof(dp));
	cout << tsp(0, 1) << "\n";

	return 0;
}