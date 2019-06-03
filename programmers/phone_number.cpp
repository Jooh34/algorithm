#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool solution(vector<string> phone_book) {
    unordered_set<string> s;
    for(string phone : phone_book) {
        s.insert(phone);
    }
    for(string phone : phone_book) {
        int len = phone.length();
        for(int i=0; i<len-1; i++) {
            string substr = phone.substr(0,i+1);
            auto got = s.find(substr);
            if (got != s.end()) { //found
                return false;
            }
        }
    }
    return true;
}

int main () {
    vector<string> phone_book{"119", "97674223", "1195524421"};
    printf("%d\n", solution(phone_book));
}
