#include <bits/stdc++.h>
using namespace std;

string braces;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	while (true) {
		getline(cin, braces);

		if (braces == ".")
			break;

		stack<char> stk;
		bool flag = true;

		for (char c : braces) {
			if (c != '(' && c != ')' && c != '[' && c != ']')
				continue;

			if (c == '(' || c == '[') {
				stk.push(c);
			}
			else if (c == ')' && stk.size() && stk.top() == '(') {
				stk.pop();
			}
			else if (c == ']' && stk.size() && stk.top() == '[') {
				stk.pop();
			}
			else {
				flag = false;
                break;
			}
		}

		if (stk.size()) flag = false;

		if (flag) cout << "yes\n"; else cout << "no\n";
	}
	return 0;
}