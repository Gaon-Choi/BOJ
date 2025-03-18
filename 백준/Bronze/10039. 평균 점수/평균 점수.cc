//https://www.acmicpc.net/problem/10039

#include <iostream>
using namespace std;

int main() {
	int score[5];
	int sum=0;
	for (int i = 0; i <= 4; i++) {
		cin >> score[i];
	}
	for (int i = 0; i <= 4; i++) {
		if (score[i] < 40) {
			score[i] = 40;
		}
		sum += score[i];
	}
	cout << sum/5;
}