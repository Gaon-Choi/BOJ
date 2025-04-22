#include <bits/stdc++.h>
using namespace std;

int t, n, m, temp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> t;

	for (int i = 0; i < t; ++i) {
		cin >> n >> m;
		vector<int> a;
		vector<int> b;

		for (int j = 0; j < n; ++j) {
			cin >> temp;
			a.push_back(temp);
		}

		for (int j = 0; j < m; ++j) {
			cin >> temp;
			b.push_back(temp);
		}

		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		int cnt = 0;

		for (int value : a) {
			cnt += (int)(lower_bound(b.begin(), b.end(), value) - b.begin());
		}

		cout << cnt << "\n";
	}

	return 0;
}