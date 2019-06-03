#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> heights) {
    int len = heights.size();

    vector<int> answer;
    answer.assign(len, 0);

    stack<int> s;
    // for 1st building
    s.push(0);

    for(int i=1; i<len; i++) {
        while(!s.empty()) {
            if(heights[s.top()] > heights[i]) { // find higher building
                answer[i] = s.top()+1;
                s.push(i);
                break;
            }
            else {
                s.pop();
            }
        }
        s.push(i);
    }

    return answer;
}

int main() {
    vector<int> heights{1,5,3,6,7,6,5};
    vector<int> answer = solution(heights);
    for (int a : answer) {
        printf("%d\n", a);
    }
}
