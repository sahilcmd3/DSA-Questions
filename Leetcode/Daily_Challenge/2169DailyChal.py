# Count Operations to Obtain Zero

"""You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

    For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However,
    if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.

Return the number of operations required to make either num1 = 0 or num2 = 0."""


# Time Complexity: O(logmax(num1,num2))
class Solution:
    def f(self, x: int, y: int, cnt: int) -> int:
        if x == 0 or y == 0:
            return cnt

        q, r = divmod(x, y)

        return self.f(y, r, cnt + q)

    def countOps(self, num1: int, num2: int) -> int:
        return self.f(num1, num2, 0)


if __name__ == "__main__":
    obj = Solution()
    print(obj.countOps(num1=2, num2=3))
