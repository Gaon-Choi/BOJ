#include <iostream>
using namespace std;
typedef long long ll;

ll a, b, c;

ll go(ll a, ll b) {
	if (b == 1) {
		return a % c;
	}

	// N번 곱셈 -> logN 번 계산
	ll ret = go (a, b / 2);

	ret = (ret * ret) % c;

	// b가 홀수인 경우 한 번 더 곱셈 진행
	if (b % 2) {
		ret = (ret * a) % c;
	}

	return ret;
}

int main() {
	// 코드 작성
	cin >> a >> b >> c;

	cout << go(a, b);

	return 0;
}