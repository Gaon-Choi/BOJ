#include <bits/stdc++.h>
using namespace std;

stack<char> stk;

string word, bomb, result;
int prev_idx = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> word;
	cin >> bomb;

	for (char c : word) {
		stk.push(c);

		if (stk.size() >= bomb.size()) {
			string temp = "";
			for (int i = 0; i < bomb.size(); ++i) {
				temp += stk.top();
				stk.pop();
			}
			reverse(temp.begin(), temp.end());

			if (temp != bomb) {
				for (char c : temp)
					stk.push(c);
			}
		}
	}

	if (stk.size()) {
		while (stk.size()) {
			result += stk.top(); stk.pop();
		}
		reverse(result.begin(), result.end());
		cout << result;
	}
	else {
		cout << "FRULA";
	}

	return 0;
}