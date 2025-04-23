#include <bits/stdc++.h>
using namespace std;

int n, a, b, l, r, cnt = 1;
vector<pair<int, int>> vec;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> a >> b;
		vec.push_back({b, a});	// 끝나는 시간 - 시작하는 시간
	}

	sort(vec.begin(), vec.end());

	l = vec[0].second; r = vec[0].first;

	for (int i = 1; i < n; ++i) {
		if (r <= vec[i].second) {
			cnt++;
			l = vec[i].second;
			r = vec[i].first;
		}
	}

	cout << cnt;

	return 0;
}