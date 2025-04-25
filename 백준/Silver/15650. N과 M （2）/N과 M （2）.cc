#include <bits/stdc++.h>
using namespace std;

int n, m;

vector<vector<int>> combination(const vector<int>& arr, int k) {
	vector<int> temp;
	vector<vector<int>> res;

	function<void(int)> backtrack = [&](int start) {
		if (temp.size() == k) {
			res.push_back(temp);
			return;
		}

		for (int i = start; i < arr.size(); ++i) {
			temp.push_back(arr[i]);
			backtrack(i + 1);
			temp.pop_back();
		}
	};

	backtrack(0);

	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n >> m;

	vector<int> arr;

	for (int num = 1; num <= n; ++num) {
		arr.push_back(num);
	}

	vector<vector<int>> result = combination(arr, m);

	for (auto vec : result) {
		for (auto v : vec) {
			cout << v << " ";
		}
		cout << "\n";
	}

	return 0;
}
