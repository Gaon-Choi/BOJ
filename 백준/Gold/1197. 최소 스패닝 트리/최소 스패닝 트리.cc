#include <bits/stdc++.h>
using namespace std;

vector<int> uf;
vector<tuple<int, int, int>> edges;

int n, m, start_node, end_node, cost;

bool cmp(tuple<int, int, int> a, tuple<int, int, int> b) {
	return get<2>(a) < get<2>(b);
}

int find_(int x) {
	if (x == uf[x]) {
		return x;
	}

	int root_node = find_(uf[x]);
	uf[x] = root_node;

	return root_node;
}

void union_(int a, int b) {
	int A = find_(a);
	int B = find_(b);

	uf[B] = A;
}

int Kruskal(vector<tuple<int, int, int>> & edges) {
	sort(edges.begin(), edges.end(), [](const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
        return get<2>(a) < get<2>(b);
    });

	int g_edge = 0;
	int mst = 0;

	for (auto edge : edges) {
		int node_a = find_(get<0>(edge));
		int node_b = find_(get<1>(edge));
		int cost = get<2>(edge);
		
		if (node_a != node_b) {
			union_(node_a, node_b);
			mst += cost;
			g_edge++;
		}

		if (g_edge == n - 1)
			break;
	}

	return mst;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n >> m;

	uf.resize(n + 1);
	iota(uf.begin(), uf.end(), 0);

	for (int i = 0; i < m; ++i) {
		cin >> start_node >> end_node >> cost;

		edges.push_back({start_node, end_node, cost});
	}

	int mst = Kruskal(edges);

	cout << mst;

	return 0;
}