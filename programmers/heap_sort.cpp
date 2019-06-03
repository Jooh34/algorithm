#include <string>
#include <vector>

using namespace std;

int size;
vector<int> arr;

void swap(int a, int b) {
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}

void heapify(int i) {
    int left=-1, right=-1, bigger=-1;

    if(2*i+2 < size) { // exist right node
        left = 2*i+1;
        right = 2*i+2;
        bigger = (arr[left]>arr[right]) ? left : right;
    }
    else if(2*i+1 < size) { // exist left node
        left = 2*i+1;
        bigger = left;
    }

    if(bigger == -1) {
        return;
    }

    if( arr[i] < arr[bigger] ) {
        swap(i,bigger);
        heapify(bigger);
    }
}

void heap_sort() {
    for(int i=size/2; i>=0; i--) {
        heapify(i);
    }
    while(size>0) {
        swap(0,size-1);
        size--;
        heapify(0);
    }
}

int main () {
    int n, num;
    scanf("%d", &n);
    while(n--) {
        scanf("%d", &num);
        arr.push_back(num);
    }
    size = arr.size();
    heap_sort();
    for(int a : arr) {
        printf("%d\n", a);
    }
}
