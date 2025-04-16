#include <bits/stdc++.h>
using namespace std;

int t, n;
string a, b;
long long res;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> t;

	while (t != 0) {
		cin >> n;

		map<string, int> map_;

		for (int i = 0; i < n; ++i) {
			cin >> a >> b;
			map_[b]++;
		}

		res = 1;

		for (auto data : map_) {
			res *= (data.second + 1);
		}

		res--;

		cout << res << "\n";

		t--;
	}


	return 0;
}