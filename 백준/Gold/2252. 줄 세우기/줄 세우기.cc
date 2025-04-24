#include <bits/stdc++.h>
using namespace std;

int n, m, src, tgt;

vector<int> topological_sort(const vector<vector<int>>& graph) {
	int n = graph.size();
	vector<int> indegree(n, 0);	// 진입 차수 배열
	vector<int> res;	// 위상 정렬 결과
	priority_queue<int, vector<int>, greater<int>> pq;	// min heap

	for (int u = 1; u < n; ++u) {
		for (int v : graph[u]) {
			indegree[v]++;
		}
	}

	for (int i = 1; i < n; ++i) {
		if (indegree[i] == 0) {
			pq.push(i);
		}
	}

	while (!pq.empty()) {
		int u = pq.top(); pq.pop();

		res.push_back(u);

		for (int v : graph[u]) {
			indegree[v]--;
			if (indegree[v] == 0) {
				pq.push(v);
			}
		}
	}

	return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n >> m;
	vector<vector<int>> graph(n + 1);

	for (int i = 0; i < m; ++i) {
		cin >> src >> tgt;
		graph[src].push_back(tgt);
	}

	vector<int> res = topological_sort(graph);

	for (auto v : res) {
		cout << v << " ";
	}

	return 0;
}