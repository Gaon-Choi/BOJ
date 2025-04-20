#include <bits/stdc++.h>
using namespace std;

const int CHICKEN = 2, HOUSE = 1, EMPTY = 0;
vector<pair<int, int>> home_list, chicken_list;
int arr[51][51], n, m, ans = 1e6;

vector<vector<int>> chickenList;

void combi(int idx, vector<int> v) {
	if (v.size() == m) {
		chickenList.push_back(v);
		return;
	}

	for (int i = idx; i < chicken_list.size(); ++i) {
		v.push_back(i);
		combi(i + 1, v);
		v.pop_back();
	}

	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> arr[i][j];
			if(arr[i][j] == HOUSE)		home_list.push_back({i, j});
			if(arr[i][j] == CHICKEN)	chicken_list.push_back({i, j});
		}
	}

	vector<int> v;
	combi(0, v);

	
	for (auto chicken_candidate : chickenList) {
		int total = 0;

		for (auto home : home_list) {
			int min_dist = 1e5;
			for (auto chicken : chicken_candidate) {
				min_dist = min(min_dist, abs(chicken_list[chicken].first - home.first) + abs(chicken_list[chicken].second - home.second));
			}
			total += min_dist;
		}

		ans = min(ans, total);
	}

	cout << ans;

	return 0;
}