# LEETCODE 1011
"""A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor
belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""


# Time complexity: O(N∗Log(Sum(Weights)))
def shipwithinDays(weights, days):
    def can_Ship(capacity):
        total = 0
        d = 1

        for w in weights:
            if total + w > capacity:
                d += 1
                total = 0

            total += w

        return d <= days

    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2

        if can_Ship(mid):
            right = mid
        else:
            left = mid + 1

    return left


print(shipwithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
