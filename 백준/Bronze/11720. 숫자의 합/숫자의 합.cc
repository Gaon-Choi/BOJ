#include <bits/stdc++.h>
using namespace std;

long n, total;
char ch;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> ch;
		total += (int)(ch - '0');
	}

	cout << total;

	return 0;
}
