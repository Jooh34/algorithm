#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e2+5, inf = 1e9;

void solve() {
    int answer[MAX] = {0,}; 

    int N,M;
    cin >> N >> M;
    for (int i=0; i<M; i++) {
        int f,t,num;
        cin >> f >> t >> num;
        for (int j=f; j<=t; j++) {
            answer[j] = num;
        }
    }

    for (int i=1; i<=N; i++) {
        cout << answer[i] << " ";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}