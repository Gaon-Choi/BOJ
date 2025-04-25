#include <bits/stdc++.h>
using namespace std;

int n, m, temp, l_point, r_point;
long long arr[10004], sum, cnt;

int main() {
	cin >> n >> m;
	
	for (int i = 0; i < n; ++i) {
		cin >> temp;
		arr[i] = temp;
	}

	l_point = 0, r_point = 0;

	while (r_point <= n) {
		if (sum == m)	cnt++;

		if (sum >= m) {
			sum -= arr[l_point];
			l_point++;
		}
		else {
			sum += arr[r_point];
			r_point++;
		}
	}

	cout << cnt;

	return 0;
}