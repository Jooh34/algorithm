#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> numbers, int target) {
    if (numbers.size() == 1) {
        if (numbers.back() == target || numbers.back() == -target) return 1;
        else return 0;
    }
    int last = numbers.back();
    numbers.pop_back();

    return solution(numbers, target + last) + solution(numbers, target - last);
}

int main () {
    int arr[] = {1,1,1,1,1};
    vector<int> numbers(arr,arr+5);

    printf("%d\n", solution(numbers, 1));
}
