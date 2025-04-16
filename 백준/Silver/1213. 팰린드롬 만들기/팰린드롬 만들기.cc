#include <bits/stdc++.h>
using namespace std;

string str;
int arr[200], flag;
string answer;
char mid;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> str;

	for (char c : str) arr[c]++;

	for (int i = 'Z'; i >= 'A'; --i) {
		// 개수가 홀수인 경우
		if (arr[i] & 1 == 1) {
			mid = char(i);
			flag++;
			arr[i]--;
		}

		// 홀수가 2개 이상 나오면 팰린드롬 만들 수 없음
		if (flag == 2)
			break;

		for (int j = 0; j < arr[i]; j += 2) {
			answer = char(i) + answer + char(i);
		}
	}

	if (mid)
		answer.insert(answer.begin() + answer.size() / 2, mid);

	if (flag == 2) {
		cout << "I'm Sorry Hansoo";
	}
	else {
		cout << answer;
	}

	return 0;
}