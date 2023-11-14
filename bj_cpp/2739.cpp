#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int N = 1e5+5, inf = 1e9;

void solve() {
    int N;
    cin >> N;

    for (int i=1; i<=9; i++) {
        cout << N << " * " << i << " = " << N*i << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}