#include <cstdio>

int main () {
  int N,X,n;
  scanf("%d%d",&N,&X);
  while(N--) {
    scanf("%d",&n);
    if(n<X) printf("%d ",n);
  }
}
