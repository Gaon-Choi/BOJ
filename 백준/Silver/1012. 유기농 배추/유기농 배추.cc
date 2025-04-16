#include <bits/stdc++.h>
using namespace std;

const int max_n = 51;

int arr[max_n][max_n], visited[max_n][max_n], t, n, m, k;
int x_, y_;

const int dxs[4] = {1, 0, -1, 0};
const int dys[4] = {0, 1, 0, -1};

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < m);
}

void bfs(int x, int y) {
	queue<pair<int, int>> q;
	visited[x][y] = 1;
	q.push({x, y});

	while (q.size()) {
		tie(x_, y_) = q.front(); q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x_ + dxs[i];
			int ny = y_ + dys[i];

			if (is_reachable(nx, ny) && (visited[nx][ny] == 0) && arr[nx][ny] == 1) {
				visited[nx][ny] = 1;
				q.push({nx, ny});
			}
		}
	}

	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> t;

	while (t) {
		cin >> n >> m >> k;

		for (int p = 0; p < k; p++) {
			cin >> x_ >> y_;
			arr[x_][y_] = 1;
		}

		int cnt = 0;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (visited[i][j] == 0 && arr[i][j] == 1) {
					bfs(i, j);
					cnt++;
				}
			}
		}

		cout << cnt << "\n";

		memset(arr, 0, sizeof(arr));
		memset(visited, 0, sizeof(visited));

		t--;
	}

	return 0;
}