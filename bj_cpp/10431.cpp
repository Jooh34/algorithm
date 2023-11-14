using namespace std;
#include <iostream>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    int N,x;
    int arr[20];

    cin >> N;
    for (int k=0; k<N; k++) {
        int answer = 0;
        cin >> x;
        for (int j=0; j<20; j++) {
            cin >> arr[j];
        }

        for (int i=1; i<20; i++) {
            int start = -1;
            for (int j=0; j<i; j++) {
                if (arr[j] > arr[i]) {
                    start = j;
                    break;
                }
            }

            int temp = arr[i];
            if (start != -1) {
                answer += (i-start);
                for (int j=i; j>start; j--) {
                    arr[j] = arr[j-1];
                }
                arr[start] = temp;
            }

        }

        cout << k+1 << " " << answer << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}