# Pow(x, n)

"""Implement pow(x, n), which calculates x raised to the power n (i.e., x^n)."""


# Time Complexity: O(log n)
# This algorithm uses binary exponentiation (divide & conquer)
class Solution:
    def calc(self, x: float, n: int) -> float:
        # Base case 1: Any number to the power 0 equals 1
        if n == 0:
            return 1

        # Base case 2: 0 to any power equals 0
        if x == 0:
            return 0

        # Divide: Calculate x^(n//2) recursively
        # Example: To find 2^8, first find 2^4
        #          To find 2^4, first find 2^2
        #          To find 2^2, first find 2^1, etc.
        res = self.calc(x, n // 2)

        # Conquer: Square the result
        # This works because: x^n = x^(n/2) * x^(n/2) = (x^(n/2))^2
        # Example: 2^8 = (2^4)^2 = 16^2 = 256
        res = res * res

        # If n is odd, we need to multiply by x one more time
        # This is because n//2 truncates: 9//2 = 4, so we lose one multiplication
        # Example: 2^9 = (2^4)^2 * 2 = 16^2 * 2 = 256 * 2 = 512
        if n % 2 == 1:
            return res * x

        # If n is even, res * res is the complete answer
        return res

    def myPow(self, x: float, n: int) -> float:
        # Calculate x^|n| (absolute value of n)
        ans = self.calc(x, abs(n))

        # If exponent is non-negative, return the result directly
        if n >= 0:
            return ans

        # If exponent is negative, return the reciprocal
        # Because: x^(-n) = 1 / x^n
        return 1 / ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.myPow(x=2.00000, n=-5))


# Tracing myPow(2, 10)
# myPow(2, 10):
# ├─ calc(2, 10)
# │   ├─ calc(2, 5)          # 10 // 2 = 5
# │   │   ├─ calc(2, 2)      # 5 // 2 = 2
# │   │   │   ├─ calc(2, 1)  # 2 // 2 = 1
# │   │   │   │   ├─ calc(2, 0) # 1//2 = 0 → returns 1  # Base case
# │   │   │   │   ├─ res = 1 * 1 = 1
# │   │   │   │   └─ n=1 is odd, so return 1 * 2 = 2
# │   │   │   ├─ res = 2 * 2 = 4
# │   │   │   └─ n=2 is even, so return 4
# │   │   ├─ res = 4 * 4 = 16
# │   │   └─ n=5 is odd, so return 16 * 2 = 32
# │   ├─ res = 32 * 32 = 1024
# │   └─ n=10 is even, so return 1024
# └─ n >= 0, so return 1024

# Result: 2^10 = 1024
