#include <bits/stdc++.h>
using namespace std;

#define rrep(n) for(int _=0;_<(n);_++)
#define rep(i,n) for(int i=0;i<(n);i++)
#define rep1(i,n) for(int i=1;i<=(n);i++)
#define repr(i,a,b) for(int i=(a);i<=(b);i++)

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int N = 1e6+1, inf = 1e9;

void solve() {
    int n,m,r;
    cin>>n>>m>>r;

    vector<int> g[N];
    int u,v;
    rrep(m) {
        cin>>u>>v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    
    rep1(i,n)
        sort(g[i].begin(), g[i].end(), greater<int>());

    deque<int> dq;
    int visited[N] = {0};

    int cnt = 1;

    dq.push_front(r);
    while (!dq.empty()) {
        int a = dq.back();
        dq.pop_back();
        if (visited[a]) continue;

        visited[a] = cnt++;

        for (int n : g[a]) {
            if (visited[n] == 0) {
                dq.push_front(n);
            }
        }
    }

    rep1(i,n)
        cout << visited[i] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}