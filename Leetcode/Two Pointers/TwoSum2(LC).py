#LEETCODE (medium)

"""Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space."""


#Time Complexity: O(n)
def two_Sum(numbers, target):
    fp = 0
    lp = len(numbers) - 1

    while fp < lp:
        total = numbers[fp] + numbers[lp]

        if total == target:
            return [fp + 1, lp + 1]
        elif total > target:
            lp -= 1
        else:
            fp += 1


ans = two_Sum(numbers=[2, 7, 11, 15], target=9)
print(ans)