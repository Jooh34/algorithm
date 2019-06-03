#include <cstdio>

int main () {
  int T,H,W;
  scanf("%d",&T);
  char meat[11][11];
  while(T--) {
    scanf("%d%d",&H,&W);
    for(int i=0; i<H; i++) {
      for(int j=0; j<W; j++) {
        scanf(" %c",&meat[i][j]);
      }
    }

    for(int i=0; i<H; i++) {
      for(int j=0; j<W; j++) {
        printf("%c",meat[H-i-1][j]);
      }
      printf("\n");
    }
  }
}
