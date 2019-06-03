#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;

    // a = w + h
    int a = (brown-4)/2;
    // b = w * h
    int b = red;

    for(int h=1; h<a; h++) {
        int w = a - h;
        if(h*w == b) {
            answer.push_back(w+2);
            answer.push_back(h+2);
            break;
        }
    }

    for (int i : answer) {
        printf("%d\n", i);
    }
    return answer;
}

int main() {
    solution(24, 24);
}
