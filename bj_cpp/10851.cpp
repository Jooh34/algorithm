#include <iostream>
#include <set>
#include <vector>
using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int N;
    cin >> N;
    set<int> s;

    for (int i=0; i<N; i++) {
        int num;
        cin >> num;
        s.insert(num);
    }

    int M;
    cin >> M;
    for (int i=0; i<M; i++) {
        int num;
        cin >> num;
        
        if (s.find(num) == s.end()) {
            cout << 0 << " ";
        }
        else {
            cout << 1 << " ";
        }
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}