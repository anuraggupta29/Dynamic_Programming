s1 = list('AGGTAB')
s2 = list('GXTXAYB')

def lcs(i = 0,j = 0):
    if (i == len(s1) or j == len(s2)):
        return 0

    elif (s1[i] == s2[j]):
        return 1 + lcs(i+1, j+1)

    else:
        return max(lcs(i+1, j), lcs(i, j+1))

#print(lcs())


def lcsDP():
    lcs_mat = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):

            if (s1[i-1] == s2[j-1]):
                lcs_mat[i][j] = 1 + lcs_mat[i-1][j-1]
            else:
                lcs_mat[i][j] = max(lcs_mat[i-1][j], lcs_mat[i][j-1])

    return lcs_mat[len(s1)][len(s2)]

print(lcsDP())
