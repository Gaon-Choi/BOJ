#include <iostream>

int a[5];

int main() {
	int sum = 0;
	for (int i = 0; i < 5; i++)
	{
		std::cin >> a[i]; sum += a[i];
	}
	std::cout << sum;
	return 0;
}