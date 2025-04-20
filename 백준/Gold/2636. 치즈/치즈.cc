#include <bits/stdc++.h>
using namespace std;

int n, m, remain_cheese, ans, temp;
int arr[101][101];
bool visited[101][101];
vector<int> vec;

const int dxs[4] = {1, 0, -1, 0};
const int dys[4] = {0, 1, 0, -1};

bool is_reachable(int x, int y) {
	return (0 <= x && x < n) && (0 <= y && y < m);
}

int dfs(int x, int y) {
	memset(visited, false, sizeof(visited));

	stack<pair<int, int>> stk;
	vector<pair<int, int>> cheese_edge;

	stk.push({x, y});
	visited[x][y] = true;

	while (stk.size()) {
		tie(x, y) = stk.top(); stk.pop();

		for (int i = 0; i < 4; ++i) {
			int nx = x + dxs[i]; int ny = y + dys[i];

			if (is_reachable(nx, ny)) {
				if (arr[nx][ny] == 1 && !visited[nx][ny]) {
					visited[nx][ny] = true;
					cheese_edge.push_back({nx, ny});
				}
				else if (arr[nx][ny] == 0 && !visited[nx][ny]) {
					visited[nx][ny] = true;
					stk.push({nx, ny});
				}
			}
		}
	}

	for (auto p : cheese_edge) {
		arr[p.first][p.second] = 0;
	}

	return cheese_edge.size();
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j)	{
			cin >> temp;
			arr[i][j] = temp;
			if (temp == 1) remain_cheese++;
		}
	}

	vec.push_back(remain_cheese);

	while (remain_cheese > 0) {
		remain_cheese -= dfs(0, 0);
		vec.push_back(remain_cheese);
		ans++;
	}

	if (ans > 0) {
		cout << ans << "\n" << vec[ans - 1];
	}
	else {
		cout << ans << "\n" << vec[ans];
	}

	return 0;
}