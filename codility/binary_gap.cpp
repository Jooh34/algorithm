#include <stdio.h>

int solution(int N) {
    int t = 32;
    int max=0,count=0;
    bool start = false;

    while (t--) {
        if(N & 1) {
            if (start) {
                if(count > max) {
                    max = count;
                }
            }
            start = true;
            count = 0;
        }
        else {
            if(start) {
                count ++;
            }
        }
        N = N >> 1;
    }
    return max;
}

int main () {
    printf("%d\n", solution(1041));
}
