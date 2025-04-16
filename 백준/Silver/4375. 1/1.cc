#include <iostream>
using namespace std;
typedef long long ll;

int n;

int main() {
	while(scanf("%d", &n) != EOF) {
		ll num = 1, ret = 1;

		while (true) {
			if (num % n == 0) {
				cout << ret << "\n";
				break;
			}
			else {
				num = (num * 10) + 1;
				num = num % n;
				ret++;
			}
		}
	}
	
	return 0;
}