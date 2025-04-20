#include <bits/stdc++.h>
using namespace std;

int num;
int n;
vector<int> ans;

int get_ten_num(int num) {
	int two = 0;
	int five = 0;

	int t = 2;

	while (t <= num) {
		two += (num / t);
		t *= 2;
	}

	t = 5;

	while (t <= num) {
		five += (num / t);
		t *= 5;
	}

	return min(two, five);
}

int main() {
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> num;
		ans.push_back(get_ten_num(num));
	}

	for (auto v : ans) {
		cout << v << "\n";
	}

	return 0;
}