# LEETCODE (medium)

"""Given an array of intervals where intervals[i] = [start i, end i], merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]."""


def merge(intervals):
    merged = []
    intervals.sort(key=lambda x: x[0])
    prev = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval

    merged.append(prev)

    return merged


print(merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
