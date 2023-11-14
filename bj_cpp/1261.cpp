using namespace std;
#include <iostream>
#include <queue>

using ll = long long;
using pii = pair<int,int>;
using pipi = pair<int,pair<int,int>>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, INF = 1e9;

int solve() {
    int N,M;
    cin >> N >> M;
    int map[100][100];
    int visited[100][100] = {0,};

    for (int i; i<M; i++) {
        string s;
        cin >> s;
        int len = s.size();
        for (int j=0; j<len; j++) {
            int num = s[j] - '0';
            map[i][j] = num;
        }
    }

    priority_queue<pipi> pq;
    pq.push(pipi(0, pii(0,0)));
    while (!pq.empty()) {
        auto p_ = pq.top();
        int cost = -p_.first;
        int i = p_.second.first; int j = p_.second.second;
        pq.pop();

        if (i == M-1 && j == N-1) {
            return cost;
        }

        if (visited[i][j]) continue;
        visited[i][j] = 1;

        vector<pii> dir = {pii(0,1), pii(0,-1), pii(1,0), pii(-1,0)};
        for (auto &d : dir) {
            int next_i = d.first+i;
            int next_j = d.second+j;

            if (0 <= next_i && next_i < M && 0 <= next_j && next_j < N) {
                if (!visited[next_i][next_j]) {
                    if (map[next_i][next_j] == 1) {
                        pq.push(pipi(-(cost+1), pii(next_i, next_j)));
                    }
                    else {
                        pq.push(pipi(-cost, pii(next_i, next_j)));
                    }
                }
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int answer = solve();
    cout << answer;
}