#include <cstdio>
#include <cmath>

typedef long long ll;

int gcd(int a, int b) {
  if(b>a) {
    int temp = a;
    a = b;
    b =temp;
  }

  int mod = a % b;

  while(mod > 0) {
    a = b;
    b = mod;
    mod = a % b;
  }

  return b;
}

ll lcm(int a, int b) {
  return a*(b/gcd(a,b));
}

int main () {
  int T,a,b;

  scanf("%d",&T);
  while(T--) {
    scanf("%d%d",&a,&b);

    int find;
    while(true) {
      find = ceil(b/a);
      while(find*a < b) {
        find++;
      }
      if(find*a == b) break;
      else {
        int l = lcm(b,find);
        a = a*l/b - l/find;
        b = l;
        int gcd_ = gcd(a,b);
        if(gcd_>1) {
          a=a/gcd_;
          b=b/gcd_;
        }
      }
    }
    printf("%d\n",find);
  }
}
