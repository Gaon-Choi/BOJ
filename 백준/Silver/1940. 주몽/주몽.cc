#include <iostream>
using namespace std;

int n, m, cnt;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	int arr[n];

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	if (m > 200000) {
		cout << 0;
	}
	else {
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				if (arr[i] + arr[j] == m)	cnt++;
			}
		}

		cout << cnt;
	}

	return 0;
}