# LEEETCODE 2226
"""You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can
divide each pile into any number of sub piles, but you cannot merge two piles together.
You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of
candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
Return the maximum number of candies each child can get."""


def maxCandies(candies, k):
    def can_distribute(mid):
        count = 0
        for pile in candies:
            count += pile // mid
        return count >= k

    low, high = 1, max(candies)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_distribute(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


print(maxCandies(candies=[5, 8, 6], k=3))
