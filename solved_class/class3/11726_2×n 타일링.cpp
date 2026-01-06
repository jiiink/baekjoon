#include <iostream>
#include <vector>
using namespace std;

int solve(int n) {
    vector<int> dp(n + 1, 0);
    
    for (int i=1; i<n+1; i++) {
        if (i == 1) {
            dp[i] = 1;
        }
        else if (i == 2) {
            dp[i] = 2;
        }
        else {
            dp[i] = (dp[i-1] + dp[i-2]) % 10007;
        }
    }

    return dp[n];
}

int main() {
    int n = 0;
    cin >> n;

    cout << solve(n) << endl;

    return 0;
}