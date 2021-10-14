def lcs(str1, str2, str3):

    string1 = len(str1)
    string2 = len(str2)
    string3 = len(str3)
    dp = [[[0 for x in range(string3+1)] for y in range(string2+1)]for z in range(string1+1)]
    for i in range(string1+1):
        for j in range(string2+1):
            for k in range(string3+1):
                if(i == 0 or j == 0 or k == 0):
                    dp[i][j][k] = 0
                elif(str1[i-1] == str2[j-1] and str1[i-1] == str3[k-1]):
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1
                else:
                    dp[i][j][k] = max(
                        max(dp[i-1][j][k], dp[i][j-1][k]), dp[i][j][k-1])
    return dp[string1][string2][string3]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    str3 = input()
    print(lcs(str1, str2, str3))


