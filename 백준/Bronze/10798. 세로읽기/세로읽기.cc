#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

char text[5][16];

int main() {
	for (int i = 0; i < 5; i++)
		std::cin >> text[i];

	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 5; j++) {
            if(text[j][i] != '\0')
			    std::cout << text[j][i];
		}
	}

	return 0;
}