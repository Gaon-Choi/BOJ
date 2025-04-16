#include <bits/stdc++.h>
using namespace std;

int c, res;
string str;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> c;

	for (int i = 0; i < c; ++i) {
		cin >> str;

		stack<char> stk;
		for (char t : str) {
			if (stk.size() && stk.top() == t) {
				stk.pop();
			}
			else {
				stk.push(t);
			}
		}

		if (stk.empty())
			res++;
	}

	cout << res;

	return 0;
}