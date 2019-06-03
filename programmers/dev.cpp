#include <string>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

queue<int> q;

int clear_queue() {
    int count = 0;
    while(!q.empty()) {
        q.pop();
        count++;
    }
    return count;
}

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int size = progresses.size();

    vector<int> fin;
    fin.assign(size, 0);

    for(int i=0; i<size; i++) { // cal finish time
        float f = (float)(100-progresses[i])/speeds[i];
        fin[i] = ceil(f);
    }

    q.push(0);

    for(int i=1; i<size; i++) {
        while(!q.empty()) {
            if(fin[q.front()] < fin[i]) {
                answer.push_back(clear_queue());
                q.push(i);
                break;
            }
            else {
                q.push(i);
                break;
            }
        }
    }
    answer.push_back(clear_queue());

    return answer;
}

int main () {
    vector<int> progresses{93,30,55};
    vector<int> speeds{1,30,5};
    vector<int> answer = solution(progresses, speeds);

    for (int a : answer) {
        printf("%d\n", a);
    }
}
