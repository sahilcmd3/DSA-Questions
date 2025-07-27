#HACKER RANK

"""You have an array (all zeros initially) and a series of instructions (called queries). Each query says,
"Add a certain value k to every number in the array between two indices a and b (inclusive)." After processing
all queries, you need to figure out the largest number in the array.

Why it Seems Tricky
If you try to directly update every element of the array for every query, it'll take too long for large arrays
or many queries. Instead, we use an efficient trick with something called a "difference array."

Step-by-Step Explanation with an Example
Let's say:
The size of the array is n = 5 (so the array starts as [0, 0, 0, 0, 0]).

You have 3 queries:
Query 1: Add 100 from index 1 to 2.
Query 2: Add 100 from index 2 to 5.
Query 3: Add 100 from index 3 to 4.

Efficient Trick (Difference Array)
Instead of updating every element directly, we do the following:
For each query:
Add the value k at index a (start of the range).
Subtract the value k at index b+1 (right after the end of the range).
This "marks" the range of influence of the query.

Why?
When we compute the prefix sum later, the additions and subtractions will automatically apply the value k to the
correct range.

Example in Action:
Start with a "difference array" (all zeros): [0, 0, 0, 0, 0, 0] (1 extra slot for b+1).

Process each query:
Query 1: Add 100 at index 1, subtract 100 at index 3 → [100, 0, -100, 0, 0, 0].
Query 2: Add 100 at index 2, subtract 100 at index 6 → [100, 100, -100, 0, 0, -100].
Query 3: Add 100 at index 3, subtract 100 at index 5 → [100, 100, 0, 0, -100, -100].

Compute the prefix sum of the array to get the final values:

Prefix sum: [100, 200, 200, 200, 100].

The maximum value in the array is 200.

Why This Is Efficient
Instead of modifying every element in the array for each query, we only make two changes per query (start and end).
Computing the prefix sum is fast, so the total time complexity is O(n + m) (where n is the array size and m is the
number of queries)."""

# Time Complexity: O(m+n)
def arrayManipulation(n, queries):
    # Initialize a difference array with zeros
    diff_array = [0] * (n + 2)  # Extra element to handle b+1

    # Apply each query using the difference array technique
    for a, b, k in queries:
        diff_array[a] += k  # Add k at index 'a'
        diff_array[b + 1] -= k  # Subtract k at index 'b+1'

    # Compute the prefix sum and find the maximum value
    max_value = 0
    current_value = 0
    for value in diff_array:
        current_value += value
        max_value = max(max_value, current_value)

    return max_value


# Example usage
n = 5
queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
result = arrayManipulation(n, queries)
print(result)