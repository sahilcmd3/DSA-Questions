# GFG Max Sum Subarray of size K
def maximumSumSubarray(nums, k):
    left = 0
    ans = 0
    sum = 0
    n = len(nums)

    for right in range(n):
        sum += nums[right]

        if right - left + 1 == k:
            ans = max(ans, sum)
            sum -= nums[left]
            left += 1

    return ans


print(maximumSumSubarray(nums=[100, 200, 300, 400], k=2))
