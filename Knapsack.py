weights = [2, 3, 4, 5]#[1, 2, 3]
profits = [1, 2, 5, 6]#[60, 100, 120]
cap = 8#5

def knapsack(weights, profits, cap):
    n = len(weights)
    dp = [[0 for i in range(cap + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, cap + 1):

            if (j - weights[i-1] < 0):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + profits[i-1])

    return dp[n][cap]

print(knapsack(weights, profits, cap))
