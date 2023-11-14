using namespace std;
#include <iostream>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 250001, inf = 1e9;

void solve() {
    int N, X;
    int arr[MAX] = {0,};
    int accum[MAX] = {0,};

    cin >> N >> X;
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }

    for (int i=1; i<=N; i++) {
        accum[i] = accum[i-1]+arr[i-1];
    }

    int num=1;
    int maxValue=0;
    for (int i=X; i<=N; i++) {
        int value = accum[i] - accum[i-X];
        if (maxValue == value) {
            num += 1;
        } else if (maxValue < value) {
            num = 1;
            maxValue = value;
        }
    }

    if (maxValue == 0) {
        cout << "SAD\n";
    } else {
        cout << maxValue << "\n" << num << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}