#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

void bfs(int n, const vector<vector<int>> &computers, vector<bool> &visited) {
    queue<int> q;
    q.push(n); //push first computer

    while(!q.empty()) {
        int cur = q.front();
        visited.at(cur) = true;

        // check unvisited computers
        vector<int> connect = computers.at(cur);
        for (size_t j=0, len2=connect.size(); j<len2; ++j) { // check all connected computers
            if (connect.at(j) && !visited.at(j)) {
                q.push(j);
            }
        }
        q.pop();
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;

    vector<bool> visited;
    visited.assign(n, false);

    for (size_t i=0, len=visited.size(); i<len; ++i) {
        if (!visited.at(i)) { // not visited yet
            answer++;
            bfs(i, computers, visited);
        }
    }

    return answer;
}

int main () {
    vector<vector<int>> computers{{1, 0, 0, 0}, {0, 1, 0, 1}, {0, 0, 1, 0}, {0, 1, 0, 1}};

    printf("\n%d\n", solution(4, computers));
}
