#include <iostream>

int hour, minute, second;
int time;

int main() {
	std::cin >> hour >> minute >> second;
	std::cin >> time;

	second += time;
	minute += (int)(second / 60);
	second %= 60;

	hour += (int)(minute / 60);
	minute %= 60;
	hour %= 24;

	std::cout << hour << " " << minute << " " << second;
	return 0;
}