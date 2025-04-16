#include <bits/stdc++.h>
using namespace std;

const int max_n = 101;

int n, m, arr[max_n][max_n], visited[max_n][max_n], x, y;

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < m);
}

int dxs[4] = {1, 0, -1, 0};
int dys[4] = {0, 1, 0, -1};

int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			scanf("%1d", &arr[i][j]);
		}
	}

	queue<pair<int, int>> q;
	visited[0][0] = 1;
	q.push({0, 0});

	while (q.size() > 0) {
		tie(x, y) = q.front(); q.pop();

		for (int i = 0; i < 4; i++) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (is_reachable(nx, ny) && (visited[nx][ny] == 0) && arr[nx][ny] == 1) {
				visited[nx][ny] = visited[x][y] + 1;
				q.push({nx, ny});
			}
		}
	}

	printf("%d", visited[n - 1][m - 1]);

	return 0;
}