#include <bits/stdc++.h>
using namespace std;

int n;
string str;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	cin >> n;
	cin.ignore();

	for (int i = 0; i < n; ++i) {
		getline(cin, str);

		int cnt[30] = {0, };
		
		for (auto c : str) {
			if ('a' <= c && c <= 'z')
				cnt[c - 'a']++;
		}

		int max_cnt = 0;

		for (auto val : cnt) {
			if (max_cnt < val) {
				max_cnt = val;
			}
		}

		vector<char> vec;

		for (int i = 0; i < 26; ++i) {
			if (cnt[i] == max_cnt)
				vec.push_back(i + 'a');
		}

		if (vec.size() == 1) {
			cout << vec[0] << "\n";
		}
		else {
			cout << "?" << "\n";
		}
	}

	return 0;
}
