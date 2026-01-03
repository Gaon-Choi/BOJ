#include <string>
#include <vector>

using namespace std;

vector<string> solution(vector<string> strArr) {
    vector<string> answer;
    
    for (string word : strArr) {
        if (word.find("ad") == string::npos) {
            answer.push_back(word);
        }
    }
    
    return answer;
}