#include <bits/stdc++.h>
using namespace std;

int n, player, one, two;
int one_time, two_time;
string timestr, prev_time = "00:00";

int string_time_to_int(string str) {
	int minute = stoi(str.substr(0, 2));
	int second = stoi(str.substr(3, 2));

	return 60 * minute + second;
}

string int_time_to_string(int time_num) {
	string minute = "00" + to_string(time_num / 60);
	string second = "00" + to_string(time_num % 60);

	return minute.substr(minute.size() - 2, 2) + ":" + second.substr(second.size() - 2, 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> player >> timestr;

		if (one > two) {
			one_time += (string_time_to_int(timestr) - string_time_to_int(prev_time));
		}
		else if (one < two) {
			two_time += (string_time_to_int(timestr) - string_time_to_int(prev_time));
		}

		if (player == 1)	one++;
		else				two++;

		prev_time = timestr;
	}

	if (one > two) {
		one_time += (string_time_to_int("48:00") - string_time_to_int(prev_time));
	}
	else if (one < two) {
		two_time += (string_time_to_int("48:00") - string_time_to_int(prev_time));
	}

	cout << int_time_to_string(one_time) << "\n" << int_time_to_string(two_time);

	return 0;
}