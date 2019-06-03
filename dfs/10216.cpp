#include <cstdio>
#include <queue>
#include <cmath>

using namespace std;

double distance(int x1, int y1, int x2, int y2) {
  return sqrt(pow(x1-x2,2)+pow(y1-y2,2));
}

int main () {
  int T,N,x,y,R;

  scanf("%d",&T);
  while(T--) {
    bool visited[3000] = {false, };
    pair<int,int> loc[3000];
    int r[3000];

    scanf("%d",&N);
    for(int i=0; i<N; i++) {
      scanf("%d%d%d",&x,&y,&R);
      loc[i].first = x;
      loc[i].second = y;
      r[i] = R;
    }

    sort(loc,loc+N);

    queue<int> q;
    int count = 0;

    for(int i=0; i<N; i++) {
      if(!visited[i]) {
        q.push(i);
        visited[i] = true;
        while(!q.empty()){ // find all connected tower
          int index = q.front();
          q.pop();

          int low = index-1;
          while(abs(loc[low].first-loc[index].first) > r[index]) { // while abs(x) < r
            if(r[index] > distance(loc[index].first, loc[index].second, loc[low].first, loc[low].second)) {
              q.push(low);
              visited[low] = true;
            }
            low--;
          }

          int high = index+1;
          while(abs(loc[high].first-loc[index].first) > r[index]) {
            if(r[index] > distance(loc[index].first, loc[index].second, loc[high].first, loc[high].second)) {
              q.push(high);
              visited[high] = true;
            }
            high++;
          }
        }
        count++;
      }
    }
  }
}
