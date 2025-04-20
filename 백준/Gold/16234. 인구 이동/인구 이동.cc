#include <bits/stdc++.h>
using namespace std;

int n, l, r, arr[101][101], visited[101][101];

const int dxs[] = {1, 0, -1, 0};
const int dys[] = {0, 1, 0, -1};

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < n);
}

bool bfs(int x, int y) {
	vector<pair<int, int>> points;
	int total = 0;

	queue<pair<int, int>> q;

	visited[x][y] = 1;
	q.push({x, y});

	while (q.size()) {
		tie(x, y) = q.front(); q.pop();
		total += arr[x][y];
		points.push_back({x, y});

		for (int i = 0; i < 4; ++i) {
			int nx = x + dxs[i]; int ny = y + dys[i];

			if (!is_reachable(nx, ny))	continue;
			if (!((l <= abs(arr[nx][ny] - arr[x][y]) && abs(arr[nx][ny] - arr[x][y]) <= r)))	continue;
			if (visited[nx][ny])	continue;

			visited[nx][ny] = 1;
			q.push({nx, ny});
		}
	}

	if (points.size() > 1) {
		int avg = total / (points.size());

		for (auto p : points) {
			arr[p.first][p.second] = avg;
		}

		return true;
	}

	return false;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> l >> r;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> arr[i][j];
		}
	}

	int cnt = 0;

	while (true) {
		bool flag = false;

		memset(visited, 0, sizeof(visited));

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (!visited[i][j])
			        flag = flag | bfs(i, j);
			}
		}

		if (!flag)	break;

		cnt++;
	}

	cout << cnt;

	return 0;
}