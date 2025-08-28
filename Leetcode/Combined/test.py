def solve(n, arr):
    """
    Find the number of pairs with even difference.
    
    Key insight: Two numbers have even difference if they have same parity
    (both even or both odd)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    even_count = 0
    odd_count = 0
    
    # Count even and odd numbers
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Calculate pairs with even difference
    # Pairs from even numbers: C(even_count, 2)
    # Pairs from odd numbers: C(odd_count, 2)
    even_pairs = (even_count * (even_count - 1)) // 2
    odd_pairs = (odd_count * (odd_count - 1)) // 2
    
    return even_pairs + odd_pairs

# Alternative one-liner approach
def solve_compact(n, arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = n - even_count
    return even_count * (even_count - 1) // 2 + odd_count * (odd_count - 1) // 2

# HackerRank input format
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = solve(n, arr)
    print(result)

# Test cases
def test_solution():
    # Test case 1
    arr1 = [2, 4, 6, 8]
    n1 = len(arr1)
    print(f"Array: {arr1}")
    print(f"Result: {solve(n1, arr1)}")
    print(f"Expected: 6 (all pairs have even difference)")
    print()
    
    # Test case 2
    arr2 = [1, 3, 5]
    n2 = len(arr2)
    print(f"Array: {arr2}")
    print(f"Result: {solve(n2, arr2)}")
    print(f"Expected: 3 (all pairs have even difference)")
    print()
    
    # Test case 3
    arr3 = [1, 2, 3, 4, 5, 6]
    n3 = len(arr3)
    print(f"Array: {arr3}")
    print(f"Result: {solve(n3, arr3)}")
    print(f"Expected: 6 (3 even pairs + 3 odd pairs)")
    print()
    
    # Test case 4
    arr4 = [1, 2]
    n4 = len(arr4)
    print(f"Array: {arr4}")
    print(f"Result: {solve(n4, arr4)}")
    print(f"Expected: 0 (different parity)")

test_solution()