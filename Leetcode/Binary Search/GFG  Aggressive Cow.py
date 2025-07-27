# GFG (Aggressive cow)
"""You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which
denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is
the maximum possible.
Examples :
Input: stalls[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at stalls[0],
the second cow can be placed at stalls[2] and
the third cow can be placed at stalls[3].
The minimum distance between cows, in this case, is 3, which also is the largest among all possible ways.
"""


def aggressiveCows(stalls, k):
    def is_possible(stalls, k, mid):
        cows_placed = 1
        last_pos = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= mid:
                cows_placed += 1
                last_pos = stalls[i]
            if cows_placed == k:
                return True

        return False

    stalls.sort()
    low, high = 1, stalls[-1] - stalls[0]
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if is_possible(stalls, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


print(aggressiveCows(stalls=[1, 2, 4, 8, 9], k=3))
