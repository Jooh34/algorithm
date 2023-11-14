using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e9, INF = 1e9;

bool compare(pii p1, pii p2) {
    return p1.first < p2.first;
}

void solve() {
    int N,L;
    cin >> N >> L;
    vector<pii> vec;

    for (int i=0; i<N; i++) {
        int u,v;
        cin >> u >> v;
        vec.push_back(pii(u,v));
    }

    sort(vec.begin(), vec.end(), compare);

    int cnt=0;
    int next=0;
    for (auto &p : vec) {
        if (p.first < next) {
            p.first = next;
        }

        int j;
        for (j=p.first; j<p.second; j+=L) {
            cnt += 1;
        }
        next = j;
    }
    
    cout << cnt << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}