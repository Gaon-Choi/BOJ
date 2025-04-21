#include <bits/stdc++.h>
using namespace std;

int n, m, sx, sy, x, y;
int arr[1001][1001];
int min_dist[1001][1001];
int visited[1001][1001];
string temp;

queue<pair<int, int>> fires;

const int WALL = 1, SPACE = 0;
const int INF = 1e6;

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < m);
}

const int dxs[] = {1, 0, -1, 0};
const int dys[] = {0, 1, 0, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j)
			min_dist[i][j] = INF;
	}

	for (int i = 0; i < n; ++i) {
		cin >> temp;
		for (int j = 0; j < m; ++j) {
			if (temp[j] == '#')			arr[i][j] = WALL;
			else if (temp[j] == 'F')	{fires.push({i, j}); min_dist[i][j] = 0;}
			else if (temp[j] == 'J')	{sx = i; sy = j;}
		}
	}

	while (fires.size()) {
		tie(x, y) = fires.front(); fires.pop();

		for (int i = 0; i < 4; ++i) {
			int nx = x + dxs[i];
			int ny = y + dys[i];

			if (is_reachable(nx, ny) && (arr[nx][ny] != WALL) && (min_dist[nx][ny] > min_dist[x][y] + 1)) {
				min_dist[nx][ny] = min_dist[x][y] + 1;
				fires.push({nx, ny});
			}
		}
	}

	queue<pair<int, int>> q;
	memset(visited, -1, sizeof(visited));

	visited[sx][sy] = 0;
	q.push({sx, sy});

	int ans = -1;

	while (q.size()) {
		tie(x, y) = q.front(); q.pop();

		if (x == 0 || x == n - 1 || y == 0 || y == m - 1) {
			ans = visited[x][y] + 1;
			break;
		}

		for (int i = 0; i < 4; ++i) {
			int nx = x + dxs[i]; int ny = y + dys[i];

			if (is_reachable(nx, ny) && arr[nx][ny] != WALL && visited[nx][ny] == -1) {
				if (visited[x][y] + 1 < min_dist[nx][ny]) {
					visited[nx][ny] = visited[x][y] + 1;
					q.push({nx, ny});
				}
			}
		}
	}

	if (ans != -1)	cout << ans;
	else			cout << "IMPOSSIBLE";

	return 0;
}