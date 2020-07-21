#include <iostream>
#include <string>
#define EE -1

int main(void) {
	int count;
	std::cin >> count;
	int size[100][20];
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 20; j++)
			size[i][j] = EE;
	std::string a, b;
	for (int i = 0; i < count; i++) {
		std::cin >> a >> b;
		for (int j = 0; j < a.size(); j++) {
			size[i][j] = char(b[j]) - char(a[j]);
			if (size[i][j] < 0) size[i][j] += 26;
		}
	}
	for (int i = 0; i < count; i++) {
		std::cout << "Distances: ";
		for (int j = 0; j < 20; j++) {
			if (size[i][j] != EE)
				std::cout << size[i][j] << " ";
		}
		if(i != count - 1)
		std::cout << std::endl;
	}
	return 0;
}