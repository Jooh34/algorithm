using namespace std;
#include <iostream>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

bool check(int x, const int* const arr, int N, int target) {
    int sum = 0;
    for (int i=0; i<N; i++) {
        sum += std::min(arr[i], x);
    }
    return sum <= target;
}


void solve() {
    int buget[100000];
    int maximum = -1;
    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> buget[i];
        maximum = max(maximum, buget[i]);
    }

    int target;
    cin >> target;

    int l=0;
    int r=maximum+1;

    while (l<r) {
        int mid = (l+r)/2;
        bool ch = check(mid, buget, N, target);
        if (ch) {
            l = mid+1;
        } else {
            r = mid;
        }
    }

    cout << l-1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}