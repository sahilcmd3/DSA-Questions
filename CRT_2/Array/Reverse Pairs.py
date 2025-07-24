# Reverse Pairs

"""Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
    0 <= i < j < nums.length and
    nums[i] > 2 * nums[j].
"""


# Merge sort and Two Pointers
# Time Complexity: O(n log n)
class Solution:
    def merge_sort(self, nums):
        # Base case: if the list is empty or has one element, it's already sorted
        if len(nums) <= 1:
            return nums, 0

        # Divide the array into two halves
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Recursively sort both halves and count reverse pairs
        left_sorted, left_count = self.merge_sort(left)
        right_sorted, right_count = self.merge_sort(right)

        # Merge both halves and count reverse pairs across the halves
        merged, merge_count = self.merge(left_sorted, right_sorted)

        # Total count is sum of left, right, and cross reverse pairs
        total_count = left_count + right_count + merge_count

        return merged, total_count

    def merge(self, left, right):
        result = []  # Final merged list
        i = j = 0
        count = 0

        # Count reverse pairs: left[i] > 2 * right[j]
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            count += j  # For each left[i], add the number of valid right[j]

        # Merge the two sorted arrays
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements from left
        while i < len(left):
            result.append(left[i])
            i += 1

        # Add remaining elements from right
        while j < len(right):
            result.append(right[j])
            j += 1

        return result, count

    def reversePairs(self, nums):
        # Run merge sort and retrieve the reverse pair count
        _, count = self.merge_sort(nums)
        return count


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.reversePairs(
            nums=[
                233,
                2000000001,
                234,
                2000000006,
                235,
                2000000003,
                236,
                2000000007,
                237,
                2000000002,
                2000000005,
                233,
                233,
                233,
                233,
                233,
                2000000004,
            ]
        )
    )


"""Time Complexity Analysis
Merge Sort: Standard merge sort has a time complexity of O(n log n) for sorting an array of size n.

Counting Reverse Pairs:
    - During the merge step, for each element in the left array, you iterate through the right array until the condition 
    left[i] > 2 * right[j] fails.
    - Because of the two-pointer strategy and the sorted nature of the arrays, this part doesn't result in a nested O(n²) loop.
    - Instead, each pointer (i, j) only moves forward across the entire array, making the reverse pair counting inside each merge step O(n).

Final Complexity: At each recursive level of merge sort, you're doing O(n) work. There are log n levels of recursion, so the total 
time complexity is: O(n log n)"""
