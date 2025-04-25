#include <bits/stdc++.h>
using namespace std;

int n, m;

vector<vector<int>> permutation_with_repetition(const vector<int>& arr, int k) {
	vector<int> temp;
	vector<vector<int>> res;

	function<void()> backtrack = [&]() {
		if (temp.size() == k) {
			res.push_back(temp);
			return;
		}

		for (int i = 0; i < arr.size(); ++i) {
			temp.push_back(arr[i]);
			backtrack();
			temp.pop_back();
		}
	};

	backtrack();

	return res;
}

int main() {
	cin >> n >> m;

	vector<int> arr;

	for (int i = 1; i <= n; ++i) {
		arr.push_back(i);
	}

	vector<vector<int>> result = permutation_with_repetition(arr, m);

	for (auto res : result) {
		for (auto num : res) {
			cout << num << " ";
		}
		cout << "\n";
	}

	return 0;
}