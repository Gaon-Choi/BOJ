#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
int n, m, src, tgt, cost;

vector<vector<int>> floyd_warshall(const vector<vector<pair<int, int>>> & graph) {
	int n = graph.size();

	vector<vector<int>> dist(n, vector<int> (n, INF));

	for (int i = 1; i < n; ++i) {
		for (int j = 1; j < n; ++j) {
			if (i != j)	continue;
			dist[i][j] = 0;
		}
	}

	for (int i = 1; i < n; ++i) {
		for (pair<int, int> p : graph[i]) {
			dist[i][p.first] = min(dist[i][p.first], p.second);
		}
	}

	for (int k = 1; k < n; ++k) {
		for (int i = 1; i < n; ++i) {
			for (int j = 1; j < n; ++j) {
				if (dist[i][k] != INF && dist[k][j] != INF) {
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}
	}

	return dist;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	cin >> m;

	vector<vector<pair<int, int>>> graph(n + 1);
	

	for (int i = 0; i < m; ++i) {
		cin >> src >> tgt >> cost;
		graph[src].push_back({tgt, cost});
	}

	vector<vector<int>> res = floyd_warshall(graph);

	for (int i = 1; i < res.size(); ++i) {
		for (int j = 1; j < res.size(); ++j) {
			if (res[i][j] != INF)
				cout << res[i][j] << " ";
			else
				cout << 0 << " ";
		}
		cout << "\n";
	}

	return 0;
}