#include <iostream>
using namespace std;

int num;
string regex, str;
string prefix, suffix;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> num;
	cin >> regex;

	prefix = regex.substr(0, regex.find('*'));
	suffix = regex.substr(regex.find('*') + 1);

	int min_size = prefix.length() + suffix.length();

	for (int i = 0; i < num; ++i) {
		cin >> str;

		if (str.size() < min_size) {
			cout << "NE" << "\n";
			continue;
		}

		if (str.substr(0, prefix.length()) == prefix && str.substr(str.length() - suffix.length()) == suffix) {
			cout << "DA" << "\n";
		}
		else {
			cout << "NE" << "\n";
		}
	}

	return 0;
}