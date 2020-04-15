#include <iostream>

void swap(int* a, int* b) {
	int temp;
	temp = *a;
	*a = *b;
	*b = temp;
	return;
}

int main(void) {
	int size, count;
	std::cin >> size >> count;
	int* arr = new int[size];
	for (int i = 0; i < size; i++)arr[i] = i + 1;
	int a, b;
	for (int i = 0; i < count; i++) {
		std::cin >> a >> b;
		swap(&arr[a - 1], &arr[b - 1]);
	}
	for (int i = 0; i < size; i++)
		std::cout << arr[i] << " ";
	delete(arr);
	return 0;
}