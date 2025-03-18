#include <iostream>

void draw(int blank, int star) {
	for (int j = 0; j < blank; j++)
		std::cout << " ";
	for (int k = 0; k < star; k++)
		std::cout << "*";
}
int main(void) {
	int d;
	std::cin >> d;
	int star = 1;
	int blank = d - 1;
	
	for (int i = 0; i < d; i++) {
		draw(blank, star);
		blank -= 1;
		star += 2;
		std::cout << std::endl;
	}
	blank += 2;
	star -= 4;
	for (int i = 0; i < d - 1; i++) {
		draw(blank, star);
		blank += 1;
		star -= 2;
		std::cout << std::endl;
	}
	return 0;
}