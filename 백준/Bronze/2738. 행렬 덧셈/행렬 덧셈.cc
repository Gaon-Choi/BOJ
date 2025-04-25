#include <bits/stdc++.h>
using namespace std;

int n, m, temp;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	vector<vector<int>> matrix(n, vector<int>(m, 0));

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> temp;
			matrix[i][j] += temp;
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cin >> temp;
			matrix[i][j] += temp;
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << matrix[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}