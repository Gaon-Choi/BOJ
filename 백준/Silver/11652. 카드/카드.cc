#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
ll n, temp;

map<ll, ll> mp;

struct Point {
	ll x, y;
};

typedef struct Point Point;

struct comp {
	bool operator()(const Point & a, const Point & b) {
		if (a.y == b.y) {
			return a.x < b.x;
		}
		return a.y > b.y;
	}
};

bool compare(const Point & a, const Point & b) {
	if (a.y == b.y) {
		return a.x < b.x;
	}
	return a.y > b.y;
}

Point pp;

vector<Point> vec;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n;

	for (ll i = 0; i < n; ++i) {
		cin >> temp;
		mp[temp]++;
	}

	for (auto p : mp) {
		pp.x = p.first;
		pp.y = p.second;
		vec.push_back(pp);
	}

	sort(vec.begin(), vec.end(), compare);

	cout << vec[0].x;

	return 0;
}