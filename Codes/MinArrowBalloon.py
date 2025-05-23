# LEETCODE (Medium)

"""There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a
2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart
and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with
xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot.
A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""


# Time Complexity: O(n log n)
# Greedy Algorithm: always shoots an arrow at the end of the current overlapping group of balloons, minimizing the total arrows needed.
def findArrow(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1])  # Sort the balloons by their ending x-coordinate (xend). 
    # This helps efficiently find overlapping balloons.

    arrows = 1
    prev_end = points[0][1]  # Started with one arrow pointed to first balloon

    for start, end in points[1:]:
        if start > prev_end:  # If its start is after the previous arrow's position (prev_end), it means the current 
            # arrow can't burst this balloon.
            arrows += 1  # Shoot a new arrow at this balloon's end, and increment the arrow count.
            prev_end = end

    return arrows


print(findArrow(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
