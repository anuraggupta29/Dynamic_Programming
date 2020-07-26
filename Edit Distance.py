s1 = 'abcd'
s2 = 'acde'

def printMat(mat):
    for i in mat:
        print(i)
    print()

def edit_distance(given_string, final_string):
    given_string = list(given_string)
    final_string = list(final_string)

    n1 = len(given_string)
    n2 = len(final_string)

    dp = [[0 for i in range(n1+1)] for j in range(n2+1)]

    for i in range(len(dp[0])):
        dp[0][i] = i

    for j in range(len(dp)):
        dp[j][0] = j

    for j in range(1, n2+1):
        for i in range(1, n1+1):
            #print(given_string[i-1], final_string[j-1])
            if (given_string[i-1] == final_string[j-1]):
                dp[j][i] = dp[j-1][i-1]
            else:
                dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
            #printMat(dp)

    ans = dp[n2][n1]
    del dp
    return ans

print(edit_distance(s1,s2))
