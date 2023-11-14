using namespace std;
#include <iostream>
#include <set>
#include <algorithm>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    set<string, greater<string>> set;
    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        string name;
        cin >> name;
        string command;
        cin >> command;

        if (command == "enter") {
            set.insert(name);
        } else {
            if (!set.empty() && set.find(name) != set.end()) {
                set.erase(name);
            }
        }
    }
    std::set<string>::iterator it;
    for (it = set.begin(); it != set.end(); it++) {
        cout << (*it) << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}