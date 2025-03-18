#include <iostream>
void draw(int star, int blank) {
	for (int i = 0; i < star; i++)
		std::cout << "*";
	for (int i = 0; i < blank; i++)
		std::cout << " ";
	for (int i = 0; i < star; i++)
		std::cout << "*";
}
int main(void) {
	int d;
	std::cin >> d;
	int star = 1;
	int blank = 2 * (d - 1);
	while (blank >= 0) {
		draw(star, blank);
		star++;
		blank -= 2;
		std::cout << std::endl;
	}
	star -= 2;
	blank += 4;
	while (star >= 0) {
		draw(star, blank);
		star--;
		blank += 2;
		std::cout << std::endl;
	}
	return 0;
}