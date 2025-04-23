#include <bits/stdc++.h>
using namespace std;

char arr[36];
int n, b, pos;
vector<char> vec;

int main() {
	for (int i = '0'; i <= '9'; ++i) {
		arr[pos++] = i;
	}

	for (int i = 'A'; i <= 'Z'; ++i) {
		arr[pos++] = i;
	}

	cin >> n >> b;

	while (n != 0) {
		vec.push_back(arr[n % b]);
		n = n / b;
	}

	reverse(vec.begin(), vec.end());

	for (auto c : vec) {
		cout << c;
	}

	return 0;
}