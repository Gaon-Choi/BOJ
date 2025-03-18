#include <iostream>
#include <cstring>
#include <math.h>
using namespace std;

int main(void) {
	int N;
	int F;
	int a = 0;
	cin >> N;
	cin >> F;
	while(1) {
		if (N / (int(pow(10, a))) == 0) {
			break;
		}
		else {
			a += 1;
		}
	}
	N -= (N % 100);
	while (1) {
		if (N % F == 0) {
			break;
		}
		else {
			N += 1;
		}
	}
	char m[10];
	sprintf(m, "%d", N);
	cout << m[strlen(m)-2] << m[strlen(m)-1];
	return 0;
}