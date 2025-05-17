### Dynamic Programming (DP)

Dynamic Programming is a powerful algorithmic technique for solving optimization problems by breaking them down
into simpler subproblems and storing the results of these subproblems to avoid redundant computations.

### Key Concepts

1. Optimal Substructure:
   - A problem has an optimal substructure if an optimal solution to the problem can be constructed from
     optimal solutions of its subproblems.

2. Overlapping Subproblems:
   - A problem has overlapping subproblems if the same subproblems are solved multiple times during the computation
     of the overall problem.

### Steps to Solve Problems Using Dynamic Programming

1. Characterize the Structure of an Optimal Solution:
   - Understand how the solution to the problem can be constructed from solutions to its subproblems.

2. Define the State:
   - Identify the variables that represent the state of the subproblems. This usually involves defining a
     function or array (often called `dp`) where `dp[i]` represents the solution to the subproblem `i`.

3. Formulate the State Transition:
   - Determine how to compute the state `dp[i]` from the states of its subproblems. This typically involves
     defining a recurrence relation.

4. Identify Base Cases:
   - Define the values of the base cases directly to terminate the recursion.

5. Implement Iteratively:
   - Iteratively compute the values of the states, starting from the base cases and working upwards
     to the final solution.

### Types of Dynamic Programming

1. Top-Down Approach (Memoization):
   - Solve the problem recursively and store the results of subproblems in a memoization table to
     avoid redundant computations.

2. Bottom-Up Approach (Tabulation):
   - Build the solution iteratively using a table, starting from the base cases and progressing
     towards the final solution.


### Recognizing When to Use Dynamic Programming

1. Optimal Substructure:
   - Check if the problem can be broken down into smaller subproblems whose solutions contribute to the
     solution of the original problem.

2. Overlapping Subproblems:
   - Check if the problem involves solving the same subproblems multiple times. If so, dynamic programming can help
     avoid redundant computations.

3. Recursive Solution:
   - If you can solve the problem recursively but encounter redundant calculations, it is a good indicator that
     dynamic programming can be applied.

### Common Patterns

1. Linear DP:
   - Problems where the state depends on a linear sequence of previous states.
   - Example: Fibonacci, Climbing Stairs.

2. 2D DP:
   - Problems involving two sequences or grids where the state depends on combinations of indices.
   - Example: Longest Common Subsequence, Edit Distance.

3. Knapsack-Like DP:
   - Problems involving selection with constraints where the state depends on the current item and remaining capacity.
   - Example: 0/1 Knapsack, Subset Sum.

4. Interval DP:
   - Problems involving intervals or subarrays where the state depends on intervals.
   - Example: Matrix Chain Multiplication, Burst Balloons.

### Conclusion

Dynamic Programming is a fundamental technique for solving a variety of problems efficiently by breaking them down
into simpler subproblems and storing their solutions. By understanding the key concepts, steps, and common patterns,
you can effectively recognize when to apply DP in LeetCode problems.


### Implementing Memoization and Tabulation

### Memoization (Top-Down Approach)

Memoization is a technique where we store the results of expensive function calls and reuse them when the same
inputs occur again. It is a top-down approach where we solve the problem recursively and store the results in a
data structure (often a dictionary or list) to avoid redundant calculations.

#### Steps for Memoization:
1. Define the base case(s).
2. Check if the current problem has been solved (i.e., if it exists in the memoization table).
3. If not solved, solve the subproblems recursively and store the result.
4. Return the stored result.

#### Example: Fibonacci Sequence with Memoization

Here's an example of how to implement the Fibonacci sequence using memoization:

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Example usage:
print(fib(10))  # Output: 55
```

### Tabulation (Bottom-Up Approach)

Tabulation is a technique where we solve the problem iteratively using a table (usually an array) to store the
results of subproblems. It is a bottom-up approach where we start from the base case(s) and build up to the
final solution.

#### Steps for Tabulation:
1. Define the base case(s) and initialize the table.
2. Iterate through the table, filling it based on the recurrence relation.
3. Return the value representing the solution to the original problem.

#### Example: Fibonacci Sequence with Tabulation

Here's an example of how to implement the Fibonacci sequence using tabulation:

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage:
print(fib(10))  # Output: 55
```

### Comparison of Memoization and Tabulation

- Memoization:
  - Uses recursion.
  - Top-down approach.
  - Stores results in a dictionary or list.
  - Can have higher space complexity due to recursion stack.
- Tabulation:
  - Uses iteration.
  - Bottom-up approach.
  - Stores results in a table (array).
  - Generally, more space efficient as it avoids recursion stack.

### Recognizing When to Use Each Approach

1. Memoization:
   - When the problem has overlapping subproblems.
   - When recursion is a natural way to represent the problem.
   - Example Problems: Fibonacci sequence, Unique paths.

2. Tabulation:
   - When the problem can be broken down into smaller subproblems that build up to the solution.
   - When an iterative solution is more intuitive or efficient.
   - Example Problems: Longest common subsequence, Knapsack problem.

### Conclusion

Both memoization and tabulation are powerful techniques in dynamic programming that help optimize solutions by
storing and reusing subproblem results. Understanding these approaches and recognizing the patterns in problems
will help you effectively apply them in LeetCode and other coding challenges.