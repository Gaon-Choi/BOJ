#include <iostream>
using namespace std;

int a, b, c, i, t;
int ns, ne;
int arr[101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> a >> b >> c;

	for (i = 0; i < 3; ++i) {
		cin >> ns >> ne;

		for (t = ns; t < ne; ++t)
			arr[t]++;
	}

	int total = 0;

	for (int v : arr) {
		if (v == 1)			total += a;
		else if (v == 2)	total += 2 * b;
		else if (v == 3)	total += 3 * c;
	}

	cout << total;

	return 0;
}