#include <iostream>
using namespace std;

int n, d[50];
int main() {
	d[1] = 1;
	for (int i = 2; i <= 45; i++) {
		d[i] = d[i - 1] + d[i - 2];
	}
	cin >> n;
	cout << d[n];
}