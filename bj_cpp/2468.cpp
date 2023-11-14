using namespace std;
#include <iostream>
#include <queue>
#include <vector>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, INF = 1e9;

int bfs(int height, int N, int map[101][101]) {
    int visited[101][101] = {0};
    int cnt = 0;

    queue<pii> q;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (visited[i][j]) continue;
            if (height >= map[i][j]) continue;

            cnt += 1;
            q.push(pii(i,j));
            while (!q.empty()) {
                pii p = q.front();
                int pi = p.first; int pj = p.second;
                q.pop();

                if (visited[pi][pj]) continue;
                visited[pi][pj] = 1;

                vector<pii> v = {pii(0,1), pii(0,-1), pii(1,0), pii(-1,0)};
                for (const pii& el : v) {
                    int next_i = pi+el.first;
                    int next_j = pj+el.second;

                    if (0<=next_i && next_i<N && 0<=next_j && next_j<N) {
                        if (height < map[pi][pj]) {
                            q.push(pii(next_i,next_j));
                        }
                    }
                }
            }
        }
    }
    return cnt;
}

void solve() {
    int map[101][101];
    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> map[i][j];
        }
    }

    int answer = 1;
    for (int k=0; k<=100; k++) {
        int cnt = bfs(k, N, map);
        answer = max(answer,cnt);
    }
    cout << answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}