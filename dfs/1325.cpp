#include <cstdio>
#include <queue>

using namespace std;

class Node {
    public:
        queue<int> slaves;
        int index;
        bool visited;
        Node() {}
        Node(int index) {
            this->index = index;
            visited = false;
        }
        void push(int n) {
            slaves.push(n);
        }
};


Node nodeList[10000];
bool result[10000];

void dfs(int idx) {
    if (nodeList[idx].visited) { // have host
        result[idx] = false;
        return;
    }
    while(!nodeList[idx].slaves.empty()) { // until queue is empty
        int slave = nodeList[idx].slaves.front();
        nodeList[idx].slaves.pop();
        dfs(slave);
    }
    nodeList[idx].visited = true;
}

int main () {
    int M,N;
    scanf("%d%d",&M,&N);

    for(int i=1; i<=N; i++) {
        nodeList[i] = Node(i);
    }
    for(int i=0; i<M; i++) {
        int a,b;
        scanf("%d%d",&a,&b);
        nodeList[b].push(a);
    }
    for(int i=1; i<=N; i++) {
        if (!nodeList[i].visited) {
            result[i] = true;
            dfs(i);
        }
    }
    for(int i=1; i<=N; i++) {
        if(result[i]) {
            printf("%d ", i);
        }
    }
}
