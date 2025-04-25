#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int n, m, src, tgt, cost;
const ll INF = 1e10;

pair<bool, vector<ll>> bellman_ford(const vector<vector<pair<ll, ll>>> & graph, ll start_node) {
	bool is_negative_cycle = false;
	
	ll n = graph.size();

	vector<ll> dist(n, INF);
	dist[start_node] = 0;

	for (ll k = 1; k < n; ++k) {
		for (ll u = 1; u < n; ++u) {
			for (pair<ll, ll> p : graph[u]) {
				ll v = p.first, cost = p.second;
				if (dist[u] != INF && dist[u] + cost < dist[v]) {
					dist[v] = dist[u] + cost;
				}
			}
		}
	}

	for (ll u = 1; u < n; ++u) {
		for (pair<ll, ll> p : graph[u]) {
			ll v = p.first, cost = p.second;
			if (dist[u] != INF && dist[u] + cost < dist[v]) {
				is_negative_cycle = true;
				break;
			}
		}

		if (is_negative_cycle) break;
	}

	// 첫번째 요소 삭제
	dist = vector<ll> (dist.begin() + 1, dist.end());

	return pair<bool, vector<ll>> (is_negative_cycle, dist);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	vector<vector<pair<ll, ll>>> graph(n + 1);

	for (int i = 0; i < m; ++i) {
		cin >> src >> tgt >> cost;
		graph[src].push_back({tgt, cost});
	}

	bool is_cycle;
	vector<ll> dist_result;

	tie(is_cycle, dist_result) = bellman_ford(graph, 1);

	if (is_cycle) {
		cout << -1;
	}
	else {
		for (int i = 1; i < n; ++i) {
			if (dist_result[i] == INF) {
				cout << -1 << "\n";
			}
			else {
				cout << dist_result[i] << "\n";
			}
		}
	}

	return 0;
}