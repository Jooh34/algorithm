using namespace std;
#include <iostream>
#include <deque>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int N;
    cin >> N;
    deque<int> dq;

    for (int i=0; i<N; i++) {
        int comm, x;
        cin >> comm;
        if (comm == 1) {
            cin >> x;
            dq.push_front(x);
        }
        else if (comm == 2) {
            cin >> x;
            dq.push_back(x);
        }
        else if (comm == 3) {
            if (dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.front() << "\n";
                dq.pop_front();
            }
        }
        else if (comm == 4) {
            if (dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.back() << "\n";
                dq.pop_back();
            }
        }
        else if (comm == 5) {
            cout << dq.size() << "\n";
        }
        else if (comm == 6) {
            if (dq.empty()) {
                cout << "1\n";
            } else {
                cout << "0\n";
            }
        }
        else if (comm == 7) {
            if (dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.front() << "\n";
            }
        }
        else if (comm == 8) {
            if (dq.empty()) {
                cout << "-1\n";
            } else {
                cout << dq.back() << "\n";
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}