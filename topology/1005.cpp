#include <cstdio>
#include <utility>
#include <queue>

using namespace std;

int main () {
  int T,N,R,X,Y,target;

  scanf("%d",&T);
  while(T--) {

    vector<int> suc[1001];
    int buildt[1001];
    int pre[1001] = {0,};
    int dp[1001] = {0,};

    scanf("%d%d",&N,&R);
    for(int i=1; i<=N; i++) scanf("%d",&buildt[i]);
    for(int i=1; i<=R; i++) {
      scanf("%d%d",&X,&Y);
      suc[X].push_back(Y);
      pre[Y]++;
    }

    scanf("%d",&target);

    queue<int> Q;
    for(int i=1; i<=N; i++)
      if(pre[i]==0) Q.push(i);

    while(pre[target] > 0) {
      int now = Q.front();
      Q.pop();

      for(int next: suc[now]) {
        dp[next] = max(dp[next], buildt[now]+dp[now]);
        pre[next]--;
        if(pre[next]==0) Q.push(next);
      }
    }

    printf("%d\n",dp[target]+buildt[target]);
  }
}
