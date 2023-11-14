using namespace std;
#include <iostream>
#include <string>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    string target;
    cin >> target;
    int n = 0;
    int i;

    for (i=1; i<=inf; i++) {
        string str = to_string(i);
        int len = int(str.size());
        for (int j=0; j<len; j++) {
            if (str[j] == target[n]) {
                n+=1;
                if (n == int(target.size())) break;
            }
        }

        if (n == int(target.size())) {
            break;
        }
    }

    cout << i << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}