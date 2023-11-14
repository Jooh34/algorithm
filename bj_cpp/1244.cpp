#include <iostream>
using namespace std;

using pii = pair<int,int>;

void solve() {
    int swt[101];
    int N,M;
    cin >> N;
    for (int i=1; i<=N; i++) {
        cin >> swt[i];
    }
    cin >> M;
    for (int i=0; i<M; i++) {
        int u,v;
        cin>>u>>v;

        if (u==1) { // men
            for (int j=v; j<=N; j+=v) {
                swt[j] ^= 1;
            }
        }
        else { // women
            int s,e,j;
            for (j=1; j<=N; j++) {
                s = v-j;
                e = v+j;
                if (s < 1 || N < e) { // out of bound
                    break;
                }
                else if (swt[s] != swt[e]) {
                    break;
                }
            }
            j--; // last success
            s = v-j;
            e = v+j;
            
            for (int k=s; k<e+1; k++) {
                swt[k] ^= 1;
            }
        }
    }

    for (int i=1; i<=N; i++) {
        cout << swt[i] << " ";
        if (i%20 == 0) {
            cout << '\n';
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}