#include <bits/stdc++.h>
using namespace std;

int n, arr[21][21];
int min_ = 987654321;

int get_one_cnt(int n) {
	int temp = n;
	int cnt = 0;

	while (temp) {
		if (temp & 1) {
			cnt++;
		}
		temp = temp / 2;
	}

	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j)	cin >> arr[i][j];
	}

	for (int i = 0; i < (1 << n); ++i) {
		if (get_one_cnt(i) != n / 2)
			continue;

		vector<int> start, link;

		for (int j = 0; j < n; ++j) {
			if (i & (1 << j)) {
				start.push_back(j);
			}
			else {
				link.push_back(j);
			}
		}

		int start_sum = 0, link_sum = 0;

		for (int i = 0; i < start.size(); ++i) {
			for (int j = i + 1; j < start.size(); ++j) {
				start_sum += (arr[start[i]][start[j]] + arr[start[j]][start[i]]);
			}
		}

		for (int i = 0; i < link.size(); ++i) {
			for (int j = i + 1; j < link.size(); ++j) {
				link_sum += (arr[link[i]][link[j]] + arr[link[j]][link[i]]);
			}
		}

		min_ = min(min_, abs(start_sum - link_sum));
	}

	cout << min_;

	return 0;
}