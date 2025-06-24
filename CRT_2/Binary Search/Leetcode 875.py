# LEETCODE 875 (KOKO eating banana)
import math


def koko(piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            right = mid  # Try a smaller speed
        else:
            left = mid + 1  # Need a larger speed

    return left


print(koko(piles=[3, 6, 7, 11], h=8))
