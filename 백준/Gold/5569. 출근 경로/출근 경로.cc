#include <iostream>

using namespace std;
long long dp[101][101][4];

int main() {
	int w, h;
	cin >> h >> w;
	int mod = 100000;
  
	for (int i = 1; i <= w; i++) {
		dp[i][1][0] = 1;
	}
	for (int j = 1; j <= h; j++) {
		dp[1][j][2] = 1;
	}

	for (int i = 2; i <= w; i++) {
		for (int j = 2; j <= h; j++) {
			dp[i][j][0] = (dp[i - 1][j][1] + dp[i - 1][j][0]) % mod;
			dp[i][j][1] = dp[i - 1][j][2];
			dp[i][j][2] = (dp[i][j - 1][3] + dp[i][j - 1][2]) % mod;
			dp[i][j][3] = dp[i][j - 1][0];
		}
	}
	int answer = 0;
	for (int k = 0; k < 4; k++) {
		answer += dp[w][h][k];
	}
	cout << answer % mod;

	return 0;
}