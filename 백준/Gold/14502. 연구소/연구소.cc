#include <bits/stdc++.h>
using namespace std;

int arr[9][9];
int n, m, temp, ans;
vector<pair<int, int>> walls;
vector<pair<int, int>> viruses;
bool visited[9][9];

const int dxs[4] = {1, 0, -1, 0};
const int dys[4] = {0, 1, 0, -1};

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < m);
}

void bfs(int x, int y) {
	queue<pair<int, int>> q;

	visited[x][y] = true;
	q.push({x, y});

	while (q.size()) {
		tie(x, y) = q.front(); q.pop();

		for (int i = 0; i < 4; ++i) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (is_reachable(nx, ny) && arr[nx][ny] == 0 && !visited[nx][ny]) {
				visited[nx][ny] = true;
				q.push({nx, ny});
			}
		}
	}
}

int bfs_all() {
	int cnt = 0;

	memset(visited, false, sizeof(visited));

	for (pair<int, int> virus : viruses) {
		bfs(virus.first, virus.second);
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (arr[i][j] == 0 && !visited[i][j]) cnt++;
		}
	}

	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> temp;
			if (temp == 0) walls.push_back({i, j});
			if (temp == 2) viruses.push_back({i, j});
			arr[i][j] = temp;
		}
	}

	for (int i = 0; i < walls.size(); ++i) {
		for (int j = i + 1; j < walls.size(); ++j) {
			for (int k = j + 1; k < walls.size(); ++k) {
				arr[walls[i].first][walls[i].second] = 1;
				arr[walls[j].first][walls[j].second] = 1;
				arr[walls[k].first][walls[k].second] = 1;

				ans = max(ans, bfs_all());

				arr[walls[i].first][walls[i].second] = 0;
				arr[walls[j].first][walls[j].second] = 0;
				arr[walls[k].first][walls[k].second] = 0;
			}
		}
	}

	cout << ans;

	return 0;
}