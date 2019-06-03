#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;

    int len=heights.size();
    answer.assign(len, 0);

    for(int i=0; i<len; ++i) {
        int num = heights.at(i);
        answer.at(i) = 0;
        for(int j=i-1; j>=0; --j) {
            if(heights.at(j) > num) {
                answer.at(i) = j+1;
                break;
            }
        }
    }

    return answer;
}

int main() {
    vector<int> heights{1,5,3,6,7,6,5};
    vector<int> answer = solution(heights);
}
