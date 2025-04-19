#include <bits/stdc++.h>
using namespace std;

int n, m, j, temp;
int bl, br;
vector<int> vec;
int total, diff;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;
	cin >> j;

	for (int i = 0; i < j; ++i) {
		cin >> temp;
		vec.push_back(temp);
	}

	bl = 1; br = bl + m - 1;

	for (int next_v : vec) {
		if (bl <= next_v && next_v <= br) {
			continue;
		}
		else if (next_v < bl) {
			diff = bl - next_v;
			bl -= diff; br -= diff;
			total += diff;
		}
		else if (next_v > br) {
			diff = next_v - br;
			bl += diff; br += diff;
			total += diff;
		}
	}

	cout << total;

	return 0;
}