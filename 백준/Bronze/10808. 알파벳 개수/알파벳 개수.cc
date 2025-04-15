#include <iostream>
using namespace std;

int arr[26];
string str;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> str;

	for (char c : str) {
		arr[c - 'a']++;
	}

	for (int v : arr) {
		cout << v << " ";
	}

	return 0;
}