# LEETCODE

"""merge two sorted arrays"""

def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    #this line removes the 0's see, m is the limit of numbers except 0 so after m numbers will be
    #replaced by numbers in second array
    nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)