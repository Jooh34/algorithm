#include <string>
#include <vector>
#include <queue>

using namespace std;

struct CustomCompare
{
    bool operator()(const vector<int> &l, const vector<int> &r)
    {
        return l[1] > r[1];
    }
};

int solution(vector<vector<int>> jobs) {
    queue<vector<int>> q;

    sort(jobs.begin(), jobs.end(),
        [](const vector<int> &l, const vector<int> &r){
            return l[0] < r[0];
        });

    for(vector<int> job : jobs) {
        q.push(job);
    }

    priority_queue<vector<int>, vector<vector<int>>, CustomCompare> pq;

    bool running = false;
    int start_time = 0;
    vector<int> cur;

    int wait_time = 0;

    for(int time=0; !q.empty() || running; ++time) {
        // stop running
        if(running) { // if running
            if(time-start_time == cur[1]) { // finish job
                running = false;
                wait_time += time-cur[0];
            }
        }
        // push job to pq that start at this time
        while(!q.empty()) {
            if(time != q.front()[0]) break;
            pq.push(q.front());
            q.pop();
        }
        // run new job from pq
        if(!running && !pq.empty()) {
            start_time = time;
            running = true;
            cur = pq.top();
            pq.pop();
        }
    }
    return wait_time/jobs.size();
}

int main() {
    vector<vector<int>> jobs{{0, 3}, {1, 9}, {2, 6}};
    printf("%d\n", solution(jobs));
}
