#include <bits/stdc++.h>
using namespace std;

int n;
int s, l, p;
vector<tuple<int, int, int>> vec;
int dp[1001][1001];
bool visited[101];

int rpg(int STR, int INT) {
	int &ret = dp[STR][INT];
	if (ret != -1) return ret;

	ret = 0;
	int pnt = 0;

	vector<int> v;

	for (int i = 0; i < n; ++i) {
		if (get<0>(vec[i]) <= STR || get<1>(vec[i]) <= INT) {
			ret++;
			if (!visited[i]) {
				visited[i] = true;
				pnt += get<2>(vec[i]);
				v.push_back(i);
			}
		}
	}

	for (int p = 0; p <= pnt; ++p) {
		int next_str = min(1000, STR + p);
		int next_int = min(1000, INT + (pnt - p));

		ret = max(ret, rpg(next_str, next_int));
	}

	for (int here : v)
		visited[here] = false;

	return ret;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> s >> l >> p;
		vec.push_back({s, l, p});
	}

	memset(dp, -1, sizeof(dp));
	cout << rpg(1, 1);

	return 0;
}