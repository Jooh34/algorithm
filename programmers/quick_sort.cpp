#include <string>
#include <vector>

using namespace std;

inline void swap(vector<int> &arr, int a, int b) {
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}

void partition(vector<int> &arr, int start, int end) {
    if(start >= end) return;

    int left = start+1;
    int right = end;
    int mid;

    int pivot = start;

    while(1) {
        while(arr[left] < arr[pivot] && left <= end) {
            left++;
        }
        while(arr[pivot] <= arr[right] && start < right) {
            right--;
        }
        if(left<=right) {
            swap(arr, left, right);
        }
        else {
            swap(arr, pivot, right);
            mid = right;
            break;
        }
    }
    partition(arr, start, mid-1);
    partition(arr, mid+1, end);
}

void quick_sort(vector<int> &arr) {
    partition(arr, 0, arr.size()-1);
}

int main () {
    vector<int> arr;

    int n, num;
    scanf("%d", &n);
    while(n--) {
        scanf("%d", &num);
        arr.push_back(num);
    }

    quick_sort(arr);
    for(int a : arr) {
        printf("%d\n", a);
    }
}
