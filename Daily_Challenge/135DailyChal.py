# LEETCODE (Hard)

"""There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

# One-Pass greedy approach: Up-Down-Peek Method
# Time complexity: O(n)
# space complexity: O(1)
def candy(ratings):
    if not ratings:
        return 0

    ret, up, down, peak = 1, 0, 0, 0

    for prev, curr in zip(ratings[:-1], ratings[1:]):
        if prev < curr:
            up, down, peak = up + 1, 0, up + 1
            ret += 1 + up
        elif prev == curr:
            up = down = peak = 0
            ret += 1
        else:
            up, down = 0, down + 1
            ret += 1 + down - int(peak >= down)

    return ret


print(candy(ratings=[1, 0, 2]))
