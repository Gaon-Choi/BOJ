#include <bits/stdc++.h>
using namespace std;

int n, c, temp;
vector<int> vec;
vector<tuple<int, int, int>> v;
map<int, int> mp;
map<int, int> mp_first_time;

// 숫자 - 빈도수 - 최초출현시점
bool cmp(tuple<int, int, int> a, tuple<int, int, int> b) {
	if (get<1>(a) == get<1>(b)) {
		return get<2>(a) < get<2>(b);
	}
	return get<1>(a) > get<1>(b);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> c;
	for (int i = 0; i < n; ++i) {
		cin >> temp;
		vec.push_back(temp);
		mp[temp]++;
		if (mp_first_time[temp] == 0) {
			mp_first_time[temp] = i + 1;
		}
	}

	for (auto it : mp) {
		v.push_back({it.first, it.second, mp_first_time[it.first]});
	}

	sort(v.begin(), v.end(), cmp);

	for (auto elem : v) {
		for (int i = 0; i < get<1>(elem); ++i) {
			cout << get<0>(elem) << " ";
		}
	}

	return 0;
}