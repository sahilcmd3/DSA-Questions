# LEETCODE 70

"""You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


# Memoization
def climbstairs(n):
    def recur(n, dp):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]

        one = recur(n - 1, dp)
        two = recur(n - 2, dp)

        dp[n] = one + two
        return dp[n]

    dp = [-1] * (n + 1)

    return recur(n, dp)


print(climbstairs(n=2))
