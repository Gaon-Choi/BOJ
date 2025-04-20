#include <iostream>
using namespace std;

int num, cnt;
int INF = 1e10;

int main() {
	cin >> num;

	for (int i = 666; i < INF; ++i) {
		if (to_string(i).find("666") != string::npos) {
			cnt++;

			if (cnt == num) {
				cout << i;
				break;
			}
		}
	}
	return 0;
}