#include <bits/stdc++.h>
using namespace std;

int n, a, b, result;
vector<pair<int, int>> vec;
priority_queue<int, vector<int>, greater<int>> pq;	// min-heap

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
		pq.push(vec[i].second);

		if (pq.size() > vec[i].first) {
			pq.pop();
		}
	}

	while (pq.size()) {
		result += pq.top();
		pq.pop();
	}

	cout << result;

	return 0;
}