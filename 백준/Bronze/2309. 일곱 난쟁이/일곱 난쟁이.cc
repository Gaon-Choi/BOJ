#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int arr[9] = {};
int k = 7;

int calculate_sum(vector<int> b) {
	int temp = 0;

	for (int elem : b)
		temp += elem;

	if (temp == 100)
		return true;

	return false;
}

void combination(int start, vector<int> & b) {
    if (b.size() == k) {
        if (calculate_sum(b)) {
			sort(b.begin(), b.end());
			for (int i : b)
				cout << i << "\n";
            
            exit(0);
		}
        
        return;
    }

    for (int i = start; i < 9; i++) {
        b.push_back(arr[i]);
        combination(i + 1, b);
        b.pop_back();
    }

    return;
}

int main() {
    ios::sync_with_stdio(false);
	cin.tie(NULL);
    
	for (int i = 0; i < 9; ++i) {
		cin >> arr[i];
	}

	vector<int> temp;

	combination(0, temp);

	return 0;
}