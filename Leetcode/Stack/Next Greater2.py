# LEETCODE 503


# Time complexity: O(n)
def nextGreater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2 * n):
        curr = nums[i % n]
        while stack and nums[stack[-1]] < curr:
            res[stack.pop()] = curr
        if i < n:
            stack.append(i)

    return res


if __name__ == "__main__":
    print(nextGreater(nums=[1, 2, 1]))
