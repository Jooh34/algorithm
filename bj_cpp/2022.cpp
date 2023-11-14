using namespace std;
#include <iostream>
#include <cmath>

using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, INF = 1e9;

double solve() {
    double x,y,c;
    cin>>x>>y>>c;
    double l = 0;
    double r = min(x,y);
    double answer = l;
    while (l+0.001<=r) {
        double mid = (l+r)/2;
        double xh = sqrt(pow(x,2) - pow(mid,2)); 
        double yh = sqrt(pow(y,2) - pow(mid,2));
        double res = (xh*yh)/(xh+yh);

        if (res >= c) {
            l = mid;
            answer = mid;
        } else {
            r = mid;
        }
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double answer = solve();
    cout << fixed;
    cout.precision(3);
    cout << answer;
}