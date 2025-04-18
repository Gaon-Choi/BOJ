#include <bits/stdc++.h>
using namespace std;

int n, m, k, i, j, x, y, cnt, area;
int sx, sy, ex, ey;

int arr[101][101];
bool visited[101][101];

const int dxs[4] = {1, 0, -1, 0};
const int dys[4] = {0, 1, 0, -1};

bool is_reachable(int x, int y) {
	return (0 <= x && x < m) && (0 <= y && y < n);
}

int bfs(int x, int y) {
	queue<pair<int, int>> q;

	int count = 0;

	visited[x][y] = true;
	q.push({x, y});

	while (q.size()) {
		tie(x, y) = q.front(); q.pop();
		count++;

		for (i = 0; i < 4; ++i) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (is_reachable(nx, ny) && (arr[nx][ny] == 0) && !visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push({nx, ny});
			}
		}
	}

	return count;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m >> k;

	for (i = 0; i < k; ++i) {
		cin >> sx >> sy >> ex >> ey;

		for (x = sx; x < ex; ++x) {
			for (y = sy; y < ey; ++y) {
				arr[x][y] = 1;
			}
		}
	}

	vector<int> vec;

	for (x = 0; x < m; ++x) {
		for (y = 0; y < n; ++y) {
			if (!visited[x][y] && arr[x][y] == 0) {
				area = bfs(x, y);
				vec.push_back(area);
				cnt += 1;
			}
		}
	}

	sort(vec.begin(), vec.end());

	cout << cnt << "\n";

	for (auto v : vec) {
		cout << v << " ";
	}

	return 0;
}