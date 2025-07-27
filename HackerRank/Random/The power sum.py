# The power sum


def powerSum(X, N):
    def countWays(target, power, num):
        val = target - num ** power
        if val == 0:
            return 1
        if val < 0:
            return 0
        return countWays(val, power, num + 1) + countWays(target, power, num + 1)

    return countWays(X, N, 1)


"""How it works:
countWays is a recursive helper that tries to subtract num^N from the target.

If the result is exactly 0, we found a valid combination.
If it goes negative, we backtrack.
We explore two paths: include num or skip it and try the next.
This approach ensures all numbers are unique and natural, as required."""
