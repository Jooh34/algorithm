#include <string>
#include <vector>

using namespace std;

vector<int> root;

int find(int x) {
    if(root[x] < 0) { // root node
        return x;
    }
    else { // not root node, track root
        return find(root[x]);
    }
}

void union_(int x, int y) {
    if (find(x) == find(y)) return;

    if (root[find(x)] <= root[find(y)]) { // size x >= size y
        root[find(x)] += root[find(y)];
        root[y] = find(x);
    }
    else { // size y > size x
        root[find(y)] += root[find(x)];
        root[x] = find(y);
    }
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    root.assign(n, -1);

    sort(costs.begin(), costs.end(),
    [](vector<int> a, vector<int> b) -> bool
    {
        return a.at(2) < b.at(2);
    });
    vector<vector<int>>::iterator it;
    for(it=costs.begin(); it!=costs.end(); ++it) {
        int x = (*it).at(0);
        int y = (*it).at(1);
        int c = (*it).at(2);
        if (find(x) == find(y)) continue;
        else {
            union_(x,y);
            answer += c;
        }
    }
    return answer;
}

int main () {
    vector<vector<int>> costs{{0,1,1},{0,2,2},{2,3,1}};
    printf("%d\n", solution(4, costs));
}
