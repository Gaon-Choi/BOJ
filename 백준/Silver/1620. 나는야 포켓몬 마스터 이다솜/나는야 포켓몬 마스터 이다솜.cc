#include <bits/stdc++.h>
using namespace std;

int n, m;
map<string, int> mymap;
vector<string> v = {""};

string temp;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> n >> m;

	for (int i = 1; i <= n; ++i) {
		cin >> temp;

		mymap[temp] = i;
		v.push_back(temp);
	}

	for (int i = 0; i < m; ++i) {
		cin >> temp;
		int idx = atoi(temp.c_str());

		// 이름
		if (idx == 0) {
			cout << mymap[temp] << "\n";
		}
		else {
			cout << v[idx] << "\n";
		}
	}

	return 0;
}