#include <bits/stdc++.h>
using namespace std;

int n;
int arr[64][64];
string s;

string quard(int x, int y, int size) {
	if (size == 1) return string(1, arr[x][y]);
	char b = arr[x][y];
	string ret = "";
	bool flag = 0;

	for (int i = x; i < x + size; ++i) {
		for (int j = y; j < y + size; ++j) {
			if (b != arr[i][j]) {
				ret += "(";
				ret += quard(x, y, size / 2);
				ret += quard(x, y + size / 2, size / 2);
				ret += quard(x + size / 2, y, size / 2);
				ret += quard(x + size / 2, y + size / 2, size / 2);
				ret += ")";
				return ret;
			}
		}
	}

	return string(1, arr[x][y]);
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> s;
		for (int j = 0; j < n; ++j) {
			arr[i][j] = s[j];
		}
	}

	cout << quard(0, 0, n) << "\n";

	return 0;
}