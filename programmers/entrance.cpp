#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;

    int max = *max_element(times.begin(), times.end());
    long long end = (long long) max * (long long)n;

    long long fit, mid, sum, start = 0;
    while (start <= end) {
        mid = (start + end) / 2;
        sum = 0;
        fit = 0;
        for (int time : times) {
            if (mid % time == 0) fit++;
            sum += mid/time;
        }
        if (n > sum) { // find right
            start = mid+1;
        }
        else if (n < sum){ // find left
            if(sum-n < fit) return mid;
            end = mid-1;
        }
        else {
            if (fit) return mid;
            else {
                end = mid-1;
            }
        }
    }
    return mid;
}

int main () {
    vector<int> times{7, 10};
    cout << solution(6, times) << endl;
}
