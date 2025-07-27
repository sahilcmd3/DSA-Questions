# Power Sum


def powerSum(X, N):
    dp = [1] + [0] * X

    for i in range(1, int(pow(X, 1 / N)) + 1):
        u = i**N
        for j in range(X, u - 1, -1):
            dp[j] += dp[j - u]

    print(dp[-1])


if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    powerSum(X, N)
