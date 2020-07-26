coins = [1, 2, 5]
sum = 5

def coinChange(coins, sum):
    n = len(coins)
    dp = [[0 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if (j - coins[i-1] < 0):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]

    return dp[n][sum]

print(coinChange(coins,sum))
