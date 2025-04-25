#include <bits/stdc++.h>
using namespace std;

int n, m;

vector<vector<int>> permutation(const vector<int>& arr, int k) {
	vector<int> temp;
	vector<vector<int>> res;
	vector<bool> visited(arr.size(), false);

	function<void()> backtrack = [&]() {
		if (temp.size() == k) {
			res.push_back(temp);
			return;
		}

		for (int i = 0; i < arr.size(); ++i) {
			if (visited[i])
				continue;
			
			visited[i] = true;
			temp.push_back(arr[i]);
			backtrack();
			temp.pop_back();
			visited[i] = false;
		}
	};

	backtrack();

	return res;
}

int main() {
	cin >> n >> m;

	vector<int> arr;

	for (int num = 1; num <= n; ++num) {
		arr.push_back(num);
	}

	vector<vector<int>> result = permutation(arr, m);

	for (auto vec : result) {
		for (auto v : vec) {
			cout << v << " ";
		}
		cout << "\n";
	}

	return 0;
}