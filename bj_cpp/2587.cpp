#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int arr[5];
    for (int i=0; i<5; i++) {
        cin >> arr[i];
    }

    int sum = 0;
    for (int i=0; i<5; i++) {
        sum += arr[i];
    }    

    sort(arr, arr+5);
    cout << sum/5 << "\n";
    cout << arr[2] << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}