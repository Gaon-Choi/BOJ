#include <bits/stdc++.h>
using namespace std;

int n;
string str, temp;
vector<string> vec;

bool comp(string str1, string str2) {
	if (str1.size() == str2.size()) {
		return str1 < str2;
	}

	return str1.size() < str2.size();
}

string preprocess(string temp) {
	while (temp.size() && temp.front() == '0') {
		temp.erase(temp.begin());
	}

	if (temp.size() == 0)
		temp = "0";

	return temp;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> str;

		for (char c : str) {
			if (c < 65) {
				temp += c;
			}
			else {
				if (temp.size()) {
					temp = preprocess(temp);
					vec.push_back(temp);
					temp.clear();
				}
			}
		}

		if (temp.size()) {
			if (temp.size()) {
				temp = preprocess(temp);
				vec.push_back(temp);
				temp.clear();
			}
		}
	}

	sort(vec.begin(), vec.end(), comp);

	for (string v : vec) {
		cout << v << "\n";
	}

	return 0;
}