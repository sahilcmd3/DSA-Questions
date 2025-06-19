# HACKER RANK MAXIMUM SUBARRAY SUM


def maximumSum(a, m):
    prefix = 0
    max_mod_sum = 0
    prefix_set = []

    def insert_sorted(val):
        # Simple binary insert
        low, high = 0, len(prefix_set)
        while low < high:
            mid = (low + high) // 2
            if prefix_set[mid] < val:
                low = mid + 1
            else:
                high = mid
        prefix_set.insert(low, val)
        return low  # Not used here, but handy if needed

    def find_greater(val):
        # First element strictly greater than val
        low, high = 0, len(prefix_set)
        while low < high:
            mid = (low + high) // 2
            if prefix_set[mid] > val:
                high = mid
            else:
                low = mid + 1
        return prefix_set[low] if low < len(prefix_set) else None

    for num in a:
        prefix = (prefix + num) % m
        max_mod_sum = max(max_mod_sum, prefix)

        next_higher = find_greater(prefix)
        if next_higher is not None:
            mod_sum = (prefix - next_higher + m) % m
            max_mod_sum = max(max_mod_sum, mod_sum)

        insert_sorted(prefix)

    return max_mod_sum


if __name__ == "__main__":
    print(maximumSum(a=[1, 2, 3], m=2))
