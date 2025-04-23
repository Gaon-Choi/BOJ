#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int n, k;

ll ret;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> k;

	vector<pair<ll, ll>> v(n);
	vector<ll> vv(k);
	priority_queue<ll> pq;

	for (int i = 0; i < n; ++i) {
		cin >> v[i].first >> v[i].second;
	}

	for (int i = 0; i < k; ++i) {
		cin >> vv[i];
	}

	sort(v.begin(), v.end());
	sort(vv.begin(), vv.end());

	int j = 0;
	for (int i = 0; i < k; ++i) {
		// 현재 가방에 담을 수 있는 보석 모두 큐에 넣음
		while (j < n && v[j].first <= vv[i]) {
			pq.push(v[j].second);
			j++;
		}

		// 가장 비용 높은 것 하나 선택
		if (pq.size()) {
			ret += pq.top();
			pq.pop();
		}
	}

	cout << ret;

	return 0;
}