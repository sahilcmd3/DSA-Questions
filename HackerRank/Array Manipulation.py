"""Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each array element between
two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.
"""


# Time Complexity: O(n+m)
def arrMan(n, queries):
    diff = [0] * (n + 1)

    # Apply range updates
    for a, b, k in queries:
        diff[a] += k
        if b + 1 <= n:
            diff[b + 1] -= k

    # Prefix sum to get final values
    max_value = 0
    current_sum = 0

    for val in diff:
        current_sum += val  # Exclude extra space
        max_value = max(max_value, current_sum)  # Prefix sum computation

    return max_value


print(arrMan(n=10, queries=[[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
