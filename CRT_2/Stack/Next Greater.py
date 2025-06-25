# Brute Force O(m*n)
"""def nextGreaterElement(nums1, nums2):
res = []
for num in nums1:
    found = False
    for i in range(len(nums2)):
        if nums2[i] == num:
            found = True
        if found and nums2[i] > num:
            res.append(nums2[i])
            break
    else:
        res.append(-1)
return res
"""


# Optimized approach: Monotonic stack (decreasing)
def nextGreaterElement(nums1, nums2):
    n = len(nums2)
    next_greater = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()
        if stack:
            next_greater[i] = stack[-1]
        stack.append(nums2[i])

    # Match results using index lookup
    res = []
    for num in nums1:
        index = nums2.index(num)
        res.append(next_greater[index])

    return res


if __name__ == "__main__":
    print(nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
