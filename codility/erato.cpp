#include <stdio.h>
#include <memory>
#include <math.h>

void erato(int n) {
    int *arr = (int *) malloc(sizeof(int) * n);
    for(int i=0; i<n; i++) {
        arr[i] = 1;
    }

    for(int i=2; i<(int)sqrt(n)+1; i++) {
        if(arr[i] == 0) continue;
        int num = i;
        while (num <= n) {
            num = num + i;
            arr[num] = 0;
        }
    }

    for (int i=2; i<n; i++) {
        if(arr[i] == 1) {
            printf("%d\n", i);
        }
    }
}

int main () {
    erato(1000);
}
