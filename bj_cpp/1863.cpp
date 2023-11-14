using namespace std;
#include <iostream>
#include <stack>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, INF = 1e9;

void solve() {
    int N;
    cin >> N;
    int A[50000];
    int B[50000];
    
    for (int i=0; i<N; i++) {
        cin >> A[i] >> B[i];
    }

    int cnt = 0;
    stack<int> stack;
    for (int i=0; i<N; i++) {
        while (!stack.empty()) {
            int top = stack.top();
            if (top > B[i]) {
                stack.pop();
                cnt += 1;
            } else if (top == B[i]) {
                stack.pop();
            }
            else {
                break;  
            }
        }
        if (B[i] != 0) {
            stack.push(B[i]);
        }
    }

    cnt += stack.size();
    cout << cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}