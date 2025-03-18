#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> prev(n);	
	// std::vector<T> name(n)
	// 기본값으로 초기화된 n개의 원소
	vector<int> end(n);
	for (int i = 0; i < n; i++) {
		std::cin >> prev[i] >> end[i];
	}
	for (int i = 0; i < n; i++)
		cout << "Case #" << i + 1 << ": " << prev[i] << " + " << end[i] << " = " << prev[i] + end[i] << endl;
	return 0;
}