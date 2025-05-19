# LEETCODE (medium)

"""Given an array of intervals where intervals[i] = [start i, end i], merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]."""


# Time Complexity: O(n log n)
def merge(intervals):
    merged = []
    # TC: O(n log n)
    intervals.sort(key=lambda x: x[0])  # Sorting ensures that when you iterate through the list, any overlapping 
    # intervals will be adjacent. This is key to the merging process because once sorted, if an interval overlaps with 
    # the previous one, you know that they belong together.
    prev = intervals[0]  # represents the current interval that is being merged with subsequent intervals if they overlap.

    # TC: O(n)
    for interval in intervals[1:]:  # Checks for overlap condition by iterating
        if interval[0] <= prev[1]:  # Overlap Condition: If the start of the current interval is less than or equal to the 
            # end of prev, then the intervals overlap. In this case, the end of prev is updated to be the maximum of its own 
            # end and the end of the current interval
            prev[1] = max(prev[1], interval[1])
        else:  # No Overlap: If the intervals do not overlap (i.e., the current interval starts after prev ends), the current 
            # prev is added to the merged list, and prev is updated to the current interval
            merged.append(prev)
            prev = interval

    merged.append(prev)

    return merged


print(merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
