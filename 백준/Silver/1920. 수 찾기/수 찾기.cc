#include <bits/stdc++.h>
using namespace std;

int n, m, temp;

int binary_search(const vector<int> & arr, int target) {
	int left = 0;
	int right = arr.size() - 1;
	int mid;

	while (left <= right) {
		mid = (left + right) / 2;

		if (arr[mid] == target) {
			return true;
		}

		if (arr[mid] < target) {
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}

	return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	vector<int> vec;
	vector<int> queries;
	vector<int> result;
	
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> temp;
		vec.push_back(temp);
	}

	cin >> m;

	for (int i = 0; i < m; ++i) {
		cin >> temp;
		queries.push_back(temp);
	}

	// 정렬
	sort(vec.begin(), vec.end());

	for (auto q : queries) {
		result.push_back(binary_search(vec, q));
	}

	for (auto res : result) {
		cout << res << "\n";
	}

	return 0;
}