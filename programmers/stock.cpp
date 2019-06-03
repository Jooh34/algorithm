#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    vector<int> answer;
    int size = prices.size();

    answer.assign(size, 0);
    stack<int> s;

    s.push(0);
    for (int i=1; i<size; ++i) {
        if (s.empty()) s.push(i);
        if(prices.at(s.top()) <= prices.at(i)) { // price up
            s.push(i);
        }
        else { // price down
            while(!s.empty()) {
                if(prices.at(s.top()) <= prices.at(i)) break;
                int idx = s.top();
                s.pop();
                answer.at(idx) = i-idx;
            }
            s.push(i);
        }
    }

    while (!s.empty()) {
        int idx = s.top();
        s.pop();
        answer.at(idx) = size-1-idx;
    }

    return answer;
}

int main () {
    vector<int> prices{1,2,3,2,3};
    vector<int> answer = solution(prices);
    for (int a : answer) {
        printf("%d\n", a);
    }
}
