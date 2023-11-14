#include <iostream>
#include <stack>

using namespace std;
using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

constexpr int MAX = 1e5+5, inf = 1e9;

void solve() {
    while (true) {
        string input;
        getline(cin, input);
        if (input == ".") {
            return;
        }

        bool answer = true;

        stack<char> stack;
        int len = input.length();
        for (int i=0; i<len; i++) {
            char ch = input[i];
            if (ch == '(' || ch == '[') {
                stack.push(ch);
            }
            else if (ch == ')') {
                if (!stack.empty() && stack.top() == '(') {
                    stack.pop();
                } else {
                    answer = false;
                    break;
                }
            } else if (ch == ']') {
                if (!stack.empty() && stack.top() == '[') {
                    stack.pop();
                } else {
                    answer = false;
                    break;
                }
            }
        }

        if (!stack.empty()) answer = false;

        if (answer) {
            cout << "yes\n";
        } else {
            cout << "no\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    solve();
}