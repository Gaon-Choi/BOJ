#include <bits/stdc++.h>
using namespace std;

string str;
int offset = 13;

int main() {
	// 공백 문자까지 모두 받아야 하므로 getline
	getline(cin, str);


	// 대문자 A는 65, 소문자 a는 97
	for (int i = 0; i < str.length(); ++i) {
		if (65 <= str[i] && str[i] <= 65 + 25) {
			str[i] = 'A' + ((str[i] - 'A' + offset) % 26);
		}
		else if (97 <= str[i] && str[i] <= 97 + 25) {
			str[i] = 'a' + ((str[i] - 'a' + offset) % 26);
		}
	}

	cout << str;

	return 0;
}