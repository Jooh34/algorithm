#include <bits/stdc++.h>
#include <stack>
using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int N;
    stack<int> stack;
    cin >> N;

    for (int i=0; i<N; i++) {
        int x;
        cin >> x;
        if (x == 1) {
            int y;
            cin >> y;
            stack.push(y);
        }
        else if (x==2) {
            if (stack.empty()) {
                cout << "-1\n";
            } else {
                cout << stack.top() << '\n';
                stack.pop();
            }
        }
        else if (x==3) {
            cout << stack.size() << '\n';
        }
        else if (x==4) {
            if (stack.empty()) {
                cout << "1\n";
            } else {
                cout << "0\n";
            }
        }
        else if (x==5) {
            if (stack.empty()) {
                cout << "-1\n";
            } else {
                cout << stack.top() << '\n';
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}