#include <bits/stdc++.h>
using namespace std;

string word;

bool is_vowel(char c) {
	return (c == 'a') || (c == 'e') || (c == 'i') || (c == 'o') || (c == 'u');
}

bool is_acceptable(string str) {
	bool is_aeiou = false;
	bool isvowel = false;
	int cnt = 0;
	char prev;

	for (char c : str) {
		if (prev == c && (prev != 'e' && prev != 'o')) {
			return false;
		}

		if (is_vowel(c)) {
			is_aeiou = true;
			if (isvowel) {
				cnt++;

				if (cnt == 3)
					return false;
			}
			else {
				isvowel = true;
				cnt = 1;
			}
		}
		else {
			if (isvowel) {
				isvowel = false;
				cnt = 1;
			}
			else {
				cnt++;

				if (cnt == 3)
					return false;
			}
		}

		prev = c;
	}

	return is_aeiou;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
	while (true) {
		cin >> word;

		if (word.compare("end") == 0)
			break;

		if (is_acceptable(word)) {
			cout << "<" << word << "> is acceptable.\n";
		}
		else {
			cout << "<" << word << "> is not acceptable.\n";
		}
	}

	return 0;
}