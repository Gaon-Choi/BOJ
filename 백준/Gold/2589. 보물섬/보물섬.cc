#include <bits/stdc++.h>
using namespace std;

int n, m, arr[51][51], visited[51][51], ans;
string temp;

const int dxs[] = {1, 0, -1, 0};
const int dys[] = {0, 1, 0, -1};

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < m);
}

void bfs(int x, int y) {
	memset(visited, 0, sizeof(visited));
	
	queue<pair<int, int>> q;
	q.push({x, y});
	visited[x][y] = 1;

	while (q.size()) {
		tie(x, y) = q.front(); q.pop();
		ans = max(ans, visited[x][y]);

		for (int i = 0; i < 4; ++i) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (!is_reachable(nx, ny))	continue;
			if (visited[nx][ny])		continue;
			if (arr[nx][ny] == 0)		continue;

			visited[nx][ny] = visited[x][y] + 1;
			q.push({nx, ny});
		}
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		cin >> temp;
		for (int j = 0; j < m; ++j) {
			if (temp[j] == 'W')	arr[i][j] = 0;
			else				arr[i][j] = 1;
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (arr[i][j] == 1)	bfs(i, j);
		}
	}

	cout << ans - 1;

	return 0;
}