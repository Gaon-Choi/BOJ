#include <bits/stdc++.h>
using namespace std;

int n, m, temp, cnt;
map<int, int> map_;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		cin >> temp;
		map_[temp]++;
	}

	for (int i = 0; i < m; ++i) {
		cin >> temp;
		map_[temp]++;
	}

	for (pair<int, int> pa : map_) {
		if (pa.second == 1)	cnt++;
	}

	cout << cnt;

	return 0;
}