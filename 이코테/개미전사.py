n = int(input())
foods = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = foods[1]

for i in range(1, n+1):
    dp[i] = max(dp[i-2]+foods[i], dp[i-1])
print(dp[n])
