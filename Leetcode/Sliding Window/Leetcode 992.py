# LEETCODE 992


def subarrK(nums, k):

    def slidingWindow(nums, k):
        n = len(nums)
        left = 0
        ans = 0
        dict = {}

        for right in range(n):
            if nums[right] not in dict:
                dict[nums[right]] = 0
            dict[nums[right]] += 1

            while len(dict) > k:
                dict[nums[left]] -= 1
                if dict[nums[left]] == 0:
                    del dict[nums[left]]
                left += 1

            ans += right - left + 1

        return ans

    def subDistinct(nums, k):
        return slidingWindow(nums, k) - slidingWindow(nums, k - 1)

    return subDistinct(nums, k)


print(subarrK(nums=[1, 2, 1, 2, 3], k=2))
