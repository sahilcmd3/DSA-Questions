# Dynamic Sliding Window
"""Window increases or decreases
Template:
    int n = s.size();
    int left = 0;
    int ans = 0;
    
    for (int right = 0; right < n; right++)
    
        // use nums[right] sum+=nums[right]
        // jab cheezein allow nhi hoti toh while loop chalega
        // while/if (window_size / requirement > 1)
        // left ko remove krdo and left++"""



# LEETCODE 3
"""Given a string s, find the length of the longest substring without duplicate characters."""

# Time Complexity: O(n)
def lenOfSub(s):
    n = len(s)
    left = 0
    ans = 0
    dict = {}
    
    for right in range(n):
        if s[right] not in dict:  # We can use dict's inbuilt function .get that checks if present add 1 else increase from 0
            dict[s[right]] = 0
        dict[s[right]] += 1
        
        while (dict[s[right]] > 1):
            dict[s[left]] -= 1
            if (dict[s[left]] == 0):
                del dict[s[left]]
                
            left += 1
    
        ans = max(ans, right - left + 1)
    
    return ans



# LEETCODE 209
"""Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose 
sum is greater than or equal to target. If there is no such subarray, return 0 instead."""

def minSub(target, nums):
    n = len(nums)
    left = 0
    ans = float('inf')  # not zero because 0 > 2 answer = 0
    sum = 0
    
    for right in range(n):
        sum += nums[right]
        
        while (sum >= target):
            ans = min(ans, right - left + 1)
            sum -= nums[left]
            left += 1
    
    return ans if ans != float('inf') else 0



# LEETCODE 904

def totalFruit(fruits):
    n = len(fruits)
    left = 0
    ans = 0
    basket = {}
    
    for right in range(n):
        if fruits[right] not in basket:
            basket[fruits[right]] = 0
        basket[fruits[right]] += 1
        
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if (basket[fruits[left]]) == 0:
                del basket[fruits[left]]
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans



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
            
            while (len(dict) > k):
                dict[nums[left]] -= 1
                if (dict[nums[left]] == 0):
                    del dict[nums[left]]
                left += 1
            
            ans += right - left + 1 

        return ans
    
    def subDistinct(nums, k):
        return slidingWindow(nums, k) - slidingWindow(nums, k - 1)
    
    return subDistinct(nums, k)



# GFG Max Sum Subarray of size K
def maximumSumSubarray(nums,k):
        # code here 
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



# LEETCODE 1004
def longestOnes(nums, k):
    n = len(nums)
    left = 0
    ans = 0
    count = {}
    
    for right in range(n):
        if nums[right] not in count:
            count[nums[right]] = 0
        count[nums[right]] += 1
        
        while 0 in count and count[0] > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans



# Fixed Sliding window
# LEETCODE 643
# LEETCODE 1456
def maxVowels(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    left = count = ans = 0

    for right in range(len(s)):
        if s[right] in vowels:
            count += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                count -= 1
            left += 1
        ans = max(ans, count)
        if ans == k:  # Can't do better
            return k

    return ans


if __name__ == "__main__":
    #print(lenOfSub(s="abcabcbb"))
    #print(minSub(target = 7, nums = [2,3,1,2,4,3]))
    #print(totalFruit(fruits = [1,2,1]))
    #print(subarrK(nums = [1,2,1,2,3], k = 2))
    #print(maximumSumSubarray(nums = [100, 200, 300, 400] , k = 2))
    #print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
    print(maxVowels(s = "abciiidef", k = 3))
