#include <bits/stdc++.h>
using namespace std;

int n, a, b, ret;
vector<pair<int, int>> vec;
priority_queue<int, vector<int>, greater<int>> pq;

int main() {
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> a >> b;
		vec.push_back({b, a});
	}

	sort(vec.begin(), vec.end());

	for (int i = 0; i < n; ++i) {
		pq.push(vec[i].second);

		// 마감일 초과하는 경우
		if (pq.size() > vec[i].first)
			pq.pop();	// 점수 가장 낮은 것 제거
	}

	while (pq.size() > 0) {
		ret += pq.top(); pq.pop();
	}

	cout << ret;

	return 0;
}