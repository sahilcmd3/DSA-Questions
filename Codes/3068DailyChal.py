# LEETCODE (Hard)

"""There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1,
where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k,
and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times
(including zero) on the tree:

Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
nums[u] = nums[u] XOR k
nums[v] = nums[v] XOR k
Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.
"""


def maxVal(nums, edges, k):
    base = sum(nums)  # Base sum & compute deltas
    deltas = [(x ^ k) - x for x in nums]
    sum_pos = cnt_pos = 0
    min_pos = float("inf")
    best_nonpos = float("-inf")

    for d in deltas:  # Collect pos deltas & track smallest pos
        if d > 0:
            cnt_pos += 1
            sum_pos += d
            min_pos = min(min_pos, d)
        else:
            best_nonpos = max(best_nonpos, d)

    if cnt_pos % 2 == 0:  # If count of positives even,
        return base + sum_pos  # then we take them all

    loss = min(min_pos, -best_nonpos)  # Else, sacrifice the smaller loss

    return base + sum_pos - loss


print(maxVal(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]]))
