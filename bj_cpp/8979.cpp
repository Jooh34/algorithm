using namespace std;
#include <iostream>
#include <tuple>
#include <vector>
#include <algorithm>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

using tiiii = tuple<int,int,int,int>;

constexpr int MAX = 1001, inf = 1e9;


void solve() {
    int N,K;
    cin >> N >> K;
    vector<tiiii> vec;

    int gold[MAX];
    int silver[MAX];
    int bronze[MAX];

    for (int i=0; i<N; i++) {
        int x,g,s,b;
        cin >> x >> g >> s >> b;
        gold[x] = g;
        silver[x] = s;
        bronze[x] = b;
    }

    int rank = 1;
    for (int i=1; i<=N; i++) {
        if (gold[i] > gold[K]) {
            rank += 1;
        }
        else if (gold[i] == gold[K]) {
            if (silver[i] > silver[K]) {
                rank += 1;
            }
            else if (silver[i] == silver[K]) {
                if (bronze[i] > bronze[K]) {
                    rank += 1;
                }
            }
        }
    }

    cout << rank;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}