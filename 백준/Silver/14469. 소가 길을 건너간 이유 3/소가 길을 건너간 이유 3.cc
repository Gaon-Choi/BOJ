#include <bits/stdc++.h>
using namespace std;

int n, a, b, res;
vector<pair<int, int>> vec;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> a >> b;
		vec.push_back({a, b});
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < n; ++i) {
		res = max(res, vec[i].first);
		res += vec[i].second;
	}

	cout << res;

	return 0;
}