#include <iostream>
#include <vector>

int main(void) {
	int a, b;
	std::vector<int> vec;
	while (true) {
		std::cin >> a >> b;
		if (std::cin.eof() == true) {
			// cin으로 입력받은 값이 없으면
			// cin.eof()는 true를 반환한다. 당연히 그렇지 않으면 false 반환
			break;
		}
		vec.emplace_back(a + b);
	}
	std::vector<int>::iterator iter;
	for (iter = vec.begin(); iter != vec.end(); iter++)
		std::cout << *iter << std::endl;
	return 0;
}