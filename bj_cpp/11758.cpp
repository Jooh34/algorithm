using namespace std;
#include <iostream>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, INF = 1e9;

int ccw(const pii &p1, const pii &p2, const pii &p3) {
    int a = p2.first-p1.first;
    int b = p2.second-p1.second;
    int c = p3.first-p2.first;
    int d = p3.second-p2.second;
    return (a*d-b*c);
}

void solve() {
    pii p1,p2,p3;
    cin >> p1.first >> p1.second;
    cin >> p2.first >> p2.second;
    cin >> p3.first >> p3.second;
    int v = ccw(p1,p2,p3);
    if (v > 0) {
        cout << 1;
    }
    else if (v < 0) {
        cout << -1;
    }
    else {
        cout << 0;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}