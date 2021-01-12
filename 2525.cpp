#include <iostream>

int hour, minute, time;

int main() {
	std::cin >> hour >> minute >> time;
	minute += time;
	hour += (minute / 60);
	minute = minute % 60;
	hour = hour % 24;

	printf("%d %d", hour, minute);
	return 0;
}