# LEETCODE (medium)

"""Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours."""



# Time Complexity: O(N∗LogM), Where N = Number Of Piles And M = Maximum Number Of Bananas In Any Pile)
# Binary Search
def eat(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        total = 0

        for pile in piles:
            total += (pile + mid - 1) // mid

        if total <= h:
            right = mid

        else:
            left = left + 1

    return left


print(eat(piles=[3, 6, 7, 11], h=8))
