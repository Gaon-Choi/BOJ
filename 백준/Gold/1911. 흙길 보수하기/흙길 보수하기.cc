#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int n, l;
ll curr_loc, a, b, res, temp, ans;

vector<pair<ll, ll>> vec;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> l;

	for (int i = 0; i < n; ++i) {
		cin >> a >> b;
		vec.push_back({a, b});
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < n; ++i) {
		if (vec[i].second <= curr_loc)	continue;

		if (curr_loc < vec[i].first) {
			temp = (vec[i].second - vec[i].first) / l + (((vec[i].second - vec[i].first) % l) != 0 ? 1 : 0);
			curr_loc = vec[i].first + l * temp;
		}
		else {
			temp = (vec[i].second - curr_loc) / l + (((vec[i].second - curr_loc) % l) != 0 ? 1 : 0);
			curr_loc += l * temp;
		}

		ans += temp;
	}

	cout << ans;

	return 0;
}