#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

queue<int> q;

int solution(vector<int> priorities, int location) {
    int count = 0;
    int len = priorities.size();

    for (int i=0; i<len; i++) {
        q.push(i);
    }

    vector<int> sorted;
    sorted.clear();
    sorted.assign(priorities.begin(), priorities.end());
    sort(sorted.begin(), sorted.end(),
        [](const int &l, const int &r){
            return l > r;
        });

    vector<int>::iterator it = sorted.begin();

    while(!q.empty()) {
        if(priorities[q.front()] == *it) { // find largest number
            count++;
            if(q.front() == location) break;
            q.pop();
            it++;
        }
        else { // find not largest number
            q.push(q.front());
            q.pop();
        }
    }
    return count;
}

int main() {
    vector<int> priorities{1, 1, 9, 1, 1, 1};
    int location = 0;
    printf("%d\n", solution(priorities, location));
}
