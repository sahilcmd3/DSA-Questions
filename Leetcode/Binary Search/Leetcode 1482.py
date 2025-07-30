# Minimum Number of Days to Make m Bouquets

"""You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make
m bouquets return -1."""


# Time Complexity: O(N∗Log(Max(Bloomday)−Min(Bloomday)))
class Solution:
    def isValid(self, mid, bloomDay, m, k):
        flowers = bouquets = 0

        for day in bloomDay:
            if day <= mid:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
                    if bouquets >= m:
                        return True
            else:
                flowers = 0

        return False

    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left <= right:
            mid = (left + right) // 2
            if self.isValid(mid, bloomDay, m, k):
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    obj = Solution()
    print(obj.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
