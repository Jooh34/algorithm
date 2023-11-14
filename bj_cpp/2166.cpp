using namespace std;
#include <iostream>
#include <cmath>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using pdd = pair<double,double>;

constexpr int MAX = 1e5+5, INF = 1e9;

double ccw(const pdd &p1, const pdd &p2, const pdd &p3) {
    double a = p2.first-p1.first;
    double b = p2.second-p1.second;
    double c = p3.first-p2.first;
    double d = p3.second-p2.second;
    return (a*d-b*c)/2;
}

void solve() {
    int N;
    cin >> N;

    pdd base, second, third;
    double u,v;
    cin>>u>>v;
    base = pdd(u,v);
    cin>>u>>v;
    second = pdd(u,v);

    double area_sum = 0;
    for (int i=0; i<N-2; i++) {
        cin>>u>>v;
        third = pdd(u,v);
        double area = ccw(base, second, third);
        area_sum += area;
        second = third;
    }

    // round .x; 
    area_sum = round(abs(area_sum)*10)/10;
    cout << fixed;
    cout.precision(1);
    cout << area_sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}