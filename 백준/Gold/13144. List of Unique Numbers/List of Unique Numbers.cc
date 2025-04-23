#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll n, ans, s, e;
ll arr[100001], cnt[100001];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}

	while (e < n) {
        if(!cnt[arr[e]]) {
            cnt[arr[e]]++;
            e++;
        }
        // 중복된 수가 있는 
        // 지금까지 탐색된 길이를 경우의 수로 저장
        else {
            ans += (e - s);
            cnt[arr[s]]--;
            s++;
        }
    }

    ans += (e - s) * (e - s + 1) / 2;
    
	cout << ans;

	return 0;
}