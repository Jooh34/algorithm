using namespace std;
#include <iostream>
#include <vector>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

int solve() {
    int N, A, B, M;
    cin >> N >> A >> B >> M;
    vector<int> graph[101];

    while (M--) {
        int u,v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int visited[101] = {0,};
    vector<pii> vec;

    vec.push_back(pii(A,0));
    visited[A] = 1;

    while (!vec.empty()) {
        pii p = vec.back();
        vec.pop_back();

        if (p.first == B) {
            return p.second;
        }

        auto next_vec = graph[p.first];
        int vecSize = next_vec.size();
        for (int j=0; j<vecSize; j++) {
            int next = next_vec[j];
            if (!visited[next]) {
                vec.push_back(pii(next, p.second+1));
                visited[next] = 1;
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int answer = solve();
    cout << answer;
}