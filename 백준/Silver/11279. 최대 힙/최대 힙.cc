#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
	priority_queue<int> pq;
	int temp;

	int num;
	cin >> num;

	for (int i = 0; i < num; ++i) {
		cin >> temp;

		if (temp == 0) {
			if (!pq.empty()) {
				cout << pq.top();
				pq.pop();
			}
			else {
				cout << 0;
			}
			cout << "\n";
		}
		else {
			pq.push(temp);
		}
	}

	return 0;
}