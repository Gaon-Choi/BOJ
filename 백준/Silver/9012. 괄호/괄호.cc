#include <bits/stdc++.h>
using namespace std;

int n;
string braces;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> braces;
		bool flag = true;
		stack<char> stk;

		for (char brace : braces) {
			if (brace == '(') {
				stk.push(brace);
			}
			else if (stk.size() && brace == ')' && stk.top() == '(') {
				stk.pop();
			}
			else {
				flag = false;
				break;
			}
		}

		if (flag && (stk.size() == 0)) cout << "YES\n"; else cout << "NO\n";
	}

	return 0;
}