import sys
sys.setrecursionlimit(10**7)

def solution(s):
    strlen = len(s)

    max = 1
    dp = [[-1] * (strlen) for i in range(strlen)]

    for i in range(strlen):
        dp[i][i] = 1

    for i in range(strlen):
        for j in range(i+1, strlen):
            if s[i] == s[j]:
                p = palindrome(dp, s,i,j)
                if max < p:
                    max = p

    return max

def palindrome(dp, s, start, end):
    if dp[start][end] != -1:
        return dp[start][end]

    if s[start] != s[end]:
        dp[start][end] = 0
        return 0
    
    else:
        if end-start == 1: # len 2 palindrome
            dp[start][end] = 2
            return 2
        
        sub = palindrome(dp, s, start+1, end-1)
        if sub == 0:
            dp[start][end] = 0
            return 0
        
        else:
            dp[start][end] = sub+2
            return sub+2
        


q1 = "abcdcba"
q2 = "abacde"
q3 = "abaacaba"
q4 = "s"*2500

print(solution(q1))
print(solution(q2))
print(solution(q3))
print(solution(q4))