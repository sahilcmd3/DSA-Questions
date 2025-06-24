# LEETCODE 167
# Time complexity: O(n)
def twoSumTwo(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total > target:
            left -= 1
        else:
            right += 1


print(twoSumTwo(numbers=[2, 7, 11, 15], target=9))
