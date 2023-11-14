using namespace std;
#include <iostream>
#include <set>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int N, M;
    cin >> N >> M;

    int answer=0;
    set<string> set;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        set.insert(s);
    }
    for (int i=0; i<M; i++) {
        string s;
        cin >> s;
        if (set.find(s) != set.end()) {
            answer += 1;
        }
    }
    cout << answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}