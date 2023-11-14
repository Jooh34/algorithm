#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

bool compare(pii p1, pii p2) {
    if (p1.first == p2.first) {
        return p1.second < p2.second;
    }
    else {
        return p1.first < p2.first;
    }
}

void solve() {
    int N;
    cin >> N;

    vector<pii> vec;
    for (int i=0; i<N; i++) {
        int u,v;
        cin >> u >> v;
        vec.push_back(pii(u,v));
    }

    sort(vec.begin(), vec.end(), compare);
    
    for (int i=0; i<N; i++) {
        pii p = vec[i];
        cout << p.first << " " << p.second << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}