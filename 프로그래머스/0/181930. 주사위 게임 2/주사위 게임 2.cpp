#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int a, int b, int c) {
    int answer = 0;
    
    int a_b = a == b;
    int a_c = a == c;
    int b_c = b == c;
    
    int sum = a_b + a_c + b_c;
    
    if (sum == 0) {
        answer = a + b + c;
    }
    else if (sum == 3) {
        answer = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2)) * (pow(a, 3) + pow(b, 3) + pow(c, 3));
    }
    else {
        answer = (a + b + c) * (pow(a, 2) + pow(b, 2) + pow(c, 2));
    }
    
    return answer;
}