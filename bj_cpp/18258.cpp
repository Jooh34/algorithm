using namespace std;
#include <iostream>
#include <queue>
#include <string>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int N;
    cin >> N;
    queue<int> q;

    for (int i=0; i<N; i++) {
        string comm;
        cin >> comm;
        if (comm == "push") {
            int x;
            cin >> x;
            q.push(x);
        }
        else if (comm == "pop") {
            if (q.empty()) {
                cout << "-1\n";
            } else {
                cout << q.front() << '\n';
                q.pop();
            }
        }
        else if (comm == "size") {
            cout << q.size() << '\n';
        }
        else if (comm == "empty") {
            if (q.empty()) {
                cout << "1\n";
            } else {
                cout << "0\n";
            }
        }
        else if (comm == "front") {
            if (q.empty()) {
                cout << "-1\n";
            } else {
                cout << q.front() << "\n";
            }
        }
        else if (comm == "back") {
            if (q.empty()) {
                cout << "-1\n";
            } else {
                cout << q.back() << "\n";
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}