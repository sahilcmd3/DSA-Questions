The slow and fast pointer approach is essentially Floyd’s Cycle Detection Algorithm, also known as Tortoise and Hare. 
This technique is used to determine whether a cycle exists in a sequence—whether in a linked list or mathematical problems like 
Happy Number.

### How They Are the Same
- You use two pointers:  
  - Slow pointer moves one step at a time.  
  - Fast pointer moves two steps at a time.  
- If a cycle exists, the fast pointer will eventually catch up to the slow pointer.
- If the fast pointer reaches `1`, then the number is happy, and we return `True`.
- If the slow pointer meets the fast pointer at a repeating number, a cycle is detected, meaning the number is not happy, 
so we return `False`.

### Why It Works
- By having a fast pointer that skips ahead, it guarantees that we won't waste extra space (unlike a hash set approach).
- This approach does not require extra memory, making it O(1) space.
- The algorithm's runtime is still O(log n) in the worst case.


Walk through an example step by step using Floyd’s Cycle Detection Algorithm (slow and fast pointers).

### Example: Checking if `19` is a Happy Number
Starting number: `19`
1. Compute next number:  
   - `1² + 9² = 1 + 81 = 82`
2. Compute next number:  
   - `8² + 2² = 64 + 4 = 68`
3. Compute next number:  
   - `6² + 8² = 36 + 64 = 100`
4. Compute next number:  
   - `1² + 0² + 0² = 1`
Reached `1` → `19` is a Happy Number!

### Using Slow and Fast Pointers
1. `slow = get_next_number(19) → 82`  
   `fast = get_next_number(get_next_number(19)) → get_next_number(82) → 68`
2. `slow = get_next_number(82) → 68`  
   `fast = get_next_number(get_next_number(68)) → get_next_number(100) → 1`
3. Since `fast == 1`, we return `True` immediately.

This approach ensures that if there’s a cycle (like in unhappy numbers), the slow and fast pointers will eventually meet 
instead of iterating infinitely. Since `19` reaches `1`, it's confirmed as a happy number!

Walk through an example where a number is not happy and falls into an infinite cycle.

### Example: Checking if `20` is a Happy Number
1. Compute next number:  
   - `2² + 0² = 4 + 0 = 4`
2. Compute next number:  
   - `4² = 16`
3. Compute next number:  
   - `1² + 6² = 1 + 36 = 37`
4. Compute next number:  
   - `3² + 7² = 9 + 49 = 58`
5. Compute next number:  
   - `5² + 8² = 25 + 64 = 89`
6. Compute next number:  
   - `8² + 9² = 64 + 81 = 145`
7. Compute next number:  
   - `1² + 4² + 5² = 1 + 16 + 25 = 42`
8. Compute next number:  
   - `4² + 2² = 16 + 4 = 20` (Back to start, cycle detected!)  

Since `20` leads back to itself in a cycle, it never reaches `1`, meaning it's not a happy number!

This is exactly why we use either the hash set approach (to track visited numbers) or Floyd’s cycle detection 
(slow and fast pointers) to efficiently detect whether a number is happy or stuck in a loop.