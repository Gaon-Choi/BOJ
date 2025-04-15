#include <bits/stdc++.h>
using namespace std;

string temp, ans;
int arr[26];
int n, i;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n;

	for (i = 0; i < n; ++i) {
		cin >> temp;
		arr[temp[0] - 'a']++;
	}

	for (i = 0; i < 26; ++i) {
		if (arr[i] >= 5)	ans += (i + 'a');
	}

	if (ans.length() > 0) {
		cout << ans;
	}
	else {
		cout << "PREDAJA";
	}

	return 0;
}