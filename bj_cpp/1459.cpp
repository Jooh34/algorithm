using namespace std;
#include <iostream>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, INF = 1e9;

void solve() {
    ll X,Y,W,S;
    cin>>X>>Y>>W>>S;
    ll answer = 0;
    if (2*W < S) {
        answer = (X+Y)*W;
    } else if (S < W) {
        answer += S*min(X,Y);
        ll remX = X - min(X,Y);
        ll remY = Y - min(X,Y);

        answer += S*(((remX+remY) / 2)*2);
        answer += W * ((X+Y)%2);
    }
    else {
        answer += S*min(X,Y);
        answer += W*abs(X-Y);
    }
    cout << answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}