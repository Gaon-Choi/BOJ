#include <iostream>
using namespace std;

int num, cnt;
int INF = 1e10;

bool has_three_six(string str) {
	for (int i = 0; i < str.size() - 2; ++i) {
		if (str.substr(i, 3) == "666")
			return true;
	}

	return false;
}

int main() {
	cin >> num;

	for (int i = 666; i < INF; ++i) {
		if (has_three_six(to_string(i))) {
			cnt++;

			if (cnt == num) {
				cout << i;
				break;
			}
		}
	}
	return 0;
}