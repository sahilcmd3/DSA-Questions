# LEETCODE (medium)

"""You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]"""


# Time Complexity: O(n log n)
def insert(intervals, newInterval):
    intervals.append(
        newInterval
    )  # By doing this, we add the new interval into the list to handle it like the other intervals.
    intervals.sort()

    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if (
            res[-1][1] >= intervals[i][0]
        ):  # checks if the last interval in res overlaps with the current interval
            # (intervals[i]). If the end of the last interval in res (res[-1][1]) is greater than or equal to the
            # start of the current interval (intervals[i][0]), then there is an overlap.
            res[-1][1] = max(
                res[-1][1], intervals[i][1]
            )  # When the intervals overlap, this line merges them by
            # updating the end of the last interval in res to be the maximum of its current end and the end of the
            # current interval. This ensures that res[-1] covers both intervals.
        else:
            res.append(intervals[i])

    return res


print(insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))


# Better Approach
# Time complexity: O(n)
"""
    res = []
    # add interval at the begininging of interval and return the result with rest of the array
    # or skip the interval and it to output
    # or merge the the new interval with the current interval

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    res.append(newInterval)
    return res"""
