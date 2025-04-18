#include <bits/stdc++.h>
using namespace std;

int n;
int i, j, h, x, y, max_cnt;

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < n);
}

int arr[101][101];
bool visited[101][101];

const int dxs[4] = {1, 0, -1, 0};
const int dys[4] = {0, 1, 0, -1};

void bfs(int x, int y, int d) {
	queue<pair<int, int>> q;

	q.push({x, y});
	visited[x][y] = true;

	while (q.size()) {
		tie(x, y) = q.front(); q.pop();
		for (i = 0; i < 4; ++i) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (is_reachable(nx, ny) && !visited[nx][ny] && arr[nx][ny] > d) {
				visited[nx][ny] = true;
				q.push({nx, ny});
			}
		}

	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;

	for (i = 0; i < n; ++i) {
		for (j = 0; j < n; ++j) {
			cin >> arr[i][j];
		}
	}

	for (h = 0; h <= 100; ++h) {
		fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);

		int cnt = 0;

		for (x = 0; x < n; ++x) {
			for (y = 0; y < n; ++y) {
				if (arr[x][y] > h && !visited[x][y]) {
					bfs(x, y, h);
					cnt++;
				}
			}
		}

		max_cnt = max(max_cnt, cnt);
	}

	cout << max_cnt;

	return 0;
}