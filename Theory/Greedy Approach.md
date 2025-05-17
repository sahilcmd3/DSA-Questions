### Greedy Approach

The greedy algorithm is an approach to solving problems by making a series of choices, each of which looks the
best at the moment (locally optimal), with the hope that these choices will lead to an overall optimal solution
(globally optimal). It doesn't always guarantee an optimal solution, but when it does, it often provides a simpler
and faster solution.

### Key Characteristics of Greedy Algorithms:
1. Local Optimality: The algorithm makes the best choice at each step.
2. Global Optimality: The local choices should lead to a globally optimal solution.
3. Non-reversibility: Once a choice is made, it cannot be undone.

### Common Patterns and Use Cases:
1. Optimization Problems: Problems where you need to find the maximum or minimum value.
   - Example: "Coin Change," "Fractional Knapsack."

2. Sorting and Scheduling: Problems that involve ordering or scheduling tasks based on certain criteria.
   - Example: "Activity Selection," "Job Sequencing."

3. Graph Problems: Certain shortest path or minimum spanning tree problems.
   - Example: "Dijkstra's Algorithm" for shortest paths, "Prim's Algorithm" for minimum spanning trees.

### Steps to Formulate a Greedy Algorithm:
1. Determine the Optimal Substructure: Ensure that the problem has an optimal substructure,
   meaning the optimal solution to the problem contains optimal solutions to subproblems.
2. Define the Greedy Choice Property: Identify the locally optimal choices that can lead to a globally optimal solution.
3. Prove the Greedy Choice: Show that making the greedy choice at every step leads to an overall optimal solution.
4. Design the Algorithm: Implement the algorithm based on the greedy choices.


### Recognizing When to Use Greedy Algorithms:

1. Optimal Substructure: The problem can be broken down into smaller problems that can be solved independently
                         and combined for a solution.
2. Greedy Choice Property: A locally optimal choice leads to a globally optimal solution.
3. Sorting: Problems where sorting the input helps to simplify the process of making greedy choices.
4. Repeated Selection: Problems involving repeated selection or ordering, such as scheduling tasks or selecting items.
5. Constraints: When the problem constraints make dynamic programming or exhaustive search impractical due to
                time or space complexity.

### Conclusion
The greedy approach is a powerful tool for solving optimization problems with certain characteristics.
By understanding the properties and common patterns of greedy algorithms, you can identify when to apply this
approach in LeetCode problems. Regular practice and analyzing different problems will help you recognize these
patterns more quickly and effectively.

### One-Pass Greedy Algorithm: Up-Down-Peak Method

# Why Up, Down, and Peak?
The essence of the one-pass greedy algorithm lies in these three variables: Up, Down, and Peak. They serve as
counters for the following:
    Up: Counts how many children have increasing ratings from the last child. This helps us determine how many candies
    we need for a child with a higher rating than the previous child.
    Down: Counts how many children have decreasing ratings from the last child. This helps us determine how many candies
    we need for a child with a lower rating than the previous child.
    Peak: Keeps track of the last highest point in an increasing sequence. When we have a decreasing sequence after the
    peak, we can refer back to the Peak to adjust the number of candies if needed.

# How Does it Work?
Initialize Your Counters
Start with ret = 1 because each child must have at least one candy. Initialize up, down, and peak to 0.
Loop Through Ratings
For each pair of adjacent children, compare their ratings. Here are the scenarios:
    If the rating is increasing: Update up and peak by incrementing them by 1. Set down to 0. Add up + 1 to ret because the
    current child must have one more candy than the previous child.
    If the rating is the same: Reset up, down, and peak to 0, because neither an increasing nor a decreasing trend is
    maintained. Add 1 to ret because the current child must have at least one candy.
    If the rating is decreasing: Update down by incrementing it by 1. Reset up to 0. Add down to ret. Additionally,
    if peak is greater than or equal to down, decrement ret by 1. This is because the peak child can share the same
    number of candies as one of the children in the decreasing sequence, which allows us to reduce the total number of
    candies.

# Return the Total Candy Count
At the end of the loop, ret will contain the minimum total number of candies needed for all the children, so return ret.
By using up, down, and peak, we can efficiently traverse the ratings list just once, updating our total candies count
(ret) as we go.