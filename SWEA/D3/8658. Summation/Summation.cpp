#include <iostream>
#include <vector>

using namespace std;

int func (int n) {
    int result = 0;
    
    while (n != 0) {
        result += (n % 10);
        n /= 10;
    }
    
    return result;
}

int main()
{
	int test_case;
	int T;
    
	cin >> T;
    int elem;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		vector<int> arr;
        
        for (int i = 0; i < 10; ++i) {
            cin >> elem;
            arr.push_back(elem);
        }
        
        vector<int> arr2;
        
        for (auto elem : arr) {
            arr2.push_back(func(elem));
        }
	
        int max_var = arr2[0];
        int min_var = arr2[0];
        
        for (auto v : arr2) {
           	if (max_var < v)	max_var = v;
            if (min_var > v)	min_var = v;
        }
        
       	std::cout << "#" << test_case << " " << max_var << " " << min_var << "\n";
	}
    
	return 0;
}