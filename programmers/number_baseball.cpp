#include <string>
#include <vector>
#include <iostream>

using namespace std;

bool check(const vector<vector<int>> &baseball, string str) {
    bool success = true;

    for (vector<int> el : baseball) {
        int s=0,b=0;
        string target = to_string(el[0]);
        if (target[0] == str[0]) s++;
        if (target[1] == str[1]) s++;
        if (target[2] == str[2]) s++;
        if (target[0] == str[1] or target[0] == str[2]) b++;
        if (target[1] == str[0] or target[1] == str[2]) b++;
        if (target[2] == str[1] or target[2] == str[0]) b++;

        if (s!=el[1] || b!=el[2]) {
            success = false;
            break;
        }
    }
    return success;
}
int solution(vector<vector<int>> baseball) {
    int answer = 0;

    for (int i=100; i<1000; ++i) {
        string s = to_string(i);
        if (s[0] == '0' || s[1] == '0' || s[2] == '0') continue;
        if (s[0] == s[1] || s[1] == s[2] || s[0] == s[2]) continue;
        if (check(baseball, s)) answer++;
    }
    return answer;
}

int main () {
    vector<vector<int>> baseball{{123, 1, 1}, {356, 1, 0}, {327, 2, 0}, {489, 0, 1}};
    printf("\n%d\n", solution(baseball));
}
