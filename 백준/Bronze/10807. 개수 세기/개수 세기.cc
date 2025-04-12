#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n;
	int elem;
	int count = 0;
	vector<int> vec = { };

	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> elem;
		vec.push_back(elem);
	}

	cin >> elem;

	for (int num : vec) {
		if (num == elem) {
			count++;
		}
	}

	cout << count;

	return 0;
}