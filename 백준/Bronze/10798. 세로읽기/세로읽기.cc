#include <bits/stdc++.h>
using namespace std;

vector<string> vec;
string temp;
int max_size;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	for (int i = 0; i < 5; ++i) {
		cin >> temp;
		
		if (max_size < temp.size()) {
			max_size = temp.size();
		}

		vec.push_back(temp);
	}

	for (int i = 0; i < max_size; ++i) {
		for (auto str : vec) {
			if (i < str.size())
				cout << str[i];
		}
	}

	return 0;
}