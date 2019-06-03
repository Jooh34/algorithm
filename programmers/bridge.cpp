#include <string>
#include <vector>
#include <queue>

using namespace std;

queue<int> q;
queue<int> trucks;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    for (int i=0; i<bridge_length; i++) {
        q.push(0);
    }
    for (int t : truck_weights) {
        trucks.push(t);
    }

    int arrived = 0;
    int time = 0;
    int size = truck_weights.size();
    int cur_w = 0;

    while(arrived < size) {
        // remove front
        if(q.front()) {
            arrived++;
            cur_w -= q.front();
        }
        q.pop();
        // push back
        if(!trucks.empty()) {
            if(cur_w + trucks.front() <= weight) {
                q.push(trucks.front());
                cur_w += trucks.front();
                trucks.pop();
            }
            else {
                q.push(0);
            }
        }
        else {
            q.push(0);
        }
        time++;
    }

    return time;
}

int main () {
    int bridge_length = 2;
    int weight = 10;
    vector<int> truck_weights{7,4,5,6};

    printf("%d\n", solution(bridge_length, weight, truck_weights));
}
