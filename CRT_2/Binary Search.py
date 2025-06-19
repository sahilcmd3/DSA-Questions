# LEETCODE 704

"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in
nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity."""

# Time complexity: O(log n)
def binSearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



# LEETCODE 35
"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the
index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""

# Time Complexity: O(log n)
def sip(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left



# LEETCODE 375
"""We are playing the Guessing Game. The game will work as follows:
    I pick a number between 1 and n.
    You guess a number.
    If you guess the right number, you win the game.
    If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
    Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
    Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
"""

"""def getmoney(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)  # Guess is the pre built api

        if res == 0:
            return mid
        elif res < 0:
            right = mid - 1
        else:
            left = mid + 1
            """


# LEETCODE 278
"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of 
your product fails the quality check. Since each version is developed based on the previous version, all the versions after 
a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first 
bad version. You should minimize the number of calls to the API."""

"""def firstbadver(n):
    low = 1
    high = n
    
    while low < high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
        
    return low"""



# LEETCODE 69
"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""

def mysqrt(x):
    low = 0
    high = x

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1

    return high



# LEETCODE 852

"""You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.
Your task is to solve it in O(log(n)) time complexity."""

# Time Complexity: O(log n)
def peakMIA(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left+right) // 2
        
        if arr [mid] > arr[mid+1]:
            right = mid  # Peak is at mid or at left
        else:
            left = mid + 1  # Peak is to the right
    return left



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



# LEETCODE 1011
"""A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor 
belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days."""

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
        
    
if __name__ == "__main__":
    #print(binSearch(nums=[-1, 0, 3, 5, 9, 12], target=9))
    #print(sip(nums=[1, 3, 5, 6], target=5))
    #print(mysqrt(x=8))
    #print(peakMIA(arr = [0,1,0]))
    #print(koko(piles = [3,6,7,11], h = 8))
    print(shipwithinDays(weights=[1,2,3,4,5,6,7,8,9,10], days = 5))
