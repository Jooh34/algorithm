#include <cstdio>
#include <cstring>

using namespace std;
typedef long long ll;

int N;
ll dp[100][100];
int board[100][100];

ll get(int i, int j) {
    if (dp[i][j] != -1) return dp[i][j];

    int v = board[i][j];
    dp[i][j] = 0;
    if (i+v < N) {
        dp[i][j] = dp[i][j] + get(i+v, j);
    }
    if (j+v < N) {
        dp[i][j] = dp[i][j] + get(i, j+v);
    }
    return dp[i][j];
}

int main () {
    scanf("%d",&N);
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            scanf("%d",&board[i][j]);
        }
    }

    memset(dp, -1, sizeof(ll) * 100 * 100);
    dp[N-1][N-1] = 1;
    printf("%lld", get(0,0));
}
