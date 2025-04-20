#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[101][101];
bool sky[101][101];
char c;

int main() {
	scanf("%d %d", &n, &m);

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			scanf("%1s", &c);
			if (c == 'c')
				sky[i][j] = true;
			else
				sky[i][j] = false;
		}
	}

	for (int i = 0; i < n; ++i) {
		int temp = -1;
		for (int j = 0; j < m; ++j) {
			if (sky[i][j]) {
				temp = 0;
			}
			else {
				if (temp != -1)
					temp++;
			}

			arr[i][j] = temp;
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}

	return 0;
}