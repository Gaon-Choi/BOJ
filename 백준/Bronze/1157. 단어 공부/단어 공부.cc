#include <bits/stdc++.h>
using namespace std;

int arr[27];
int max_ = -1;
vector<char> ans;
string word;

int main() {
	cin >> word;

	for (char c : word) {
		if (c >= 97) {
			arr[c - 97]++;
		}
		else {
			arr[c - 65]++;
		}
	}

	for (int i = 0; i < 27; ++i) {
		if (max_ < arr[i])
			max_ = arr[i];
	}

	for (int i = 0; i < 27; ++i) {
		if (max_ == arr[i])
			ans.push_back(i + 65);
	}

	if (ans.size() > 1) {
		cout << "?";
	}
	else {
		cout << ans[0];
	}

	return 0;
}