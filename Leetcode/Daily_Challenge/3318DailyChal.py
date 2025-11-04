# Find X-Sum of All K-Long Subarrays I

"""You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:
    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences,
    the element with the bigger value is considered more frequent.
    Calculate the sum of the resulting array.

Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1]."""

from collections import Counter


class Solution:
    def findSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        result: list[int] = []

        for i in range(n - k + 1):
            window = nums[i : i + k]
            freq = Counter(window)
            sorted_freq = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))
            top_x = set(num for num, _ in sorted_freq[:x])
            x_sum = sum(num for num in window if num in top_x)
            result.append(x_sum)

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.findSum(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
