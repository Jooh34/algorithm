using namespace std;
#include <iostream>
#include <queue>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1000000+1, INF = 1e9;

int solve() {
    int F,S,G,U,D;
    cin >> F >> S >> G >> U >> D;
    queue<pii> q;
    
    int dist[MAX];
    fill_n(dist, MAX, INF);

    q.push(pii(S,0));
    while (!q.empty()) {
        pii p = q.front();
        int i = p.first; int c = p.second;
        // cout << i << " " << c << "\n";
        q.pop();

        if (i == G) return c;

        if (dist[i] <= c) continue;
        dist[i] = c;

        // up
        int next = i+U;
        int next_c = c+1;
        if (next <= F) {
            if (dist[next] > next_c) {
                q.push(pii(next,next_c));
            }
        }

        next = i-D;
        if (1 <= next) {
            if (dist[next] > next_c) {
                q.push(pii(next,next_c));
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int answer = solve();
    if (answer == -1) {
        cout << "use the stairs\n";
    } else {
        cout << answer;
    }
}