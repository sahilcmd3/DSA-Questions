# HackerRank -> Bigger is Greater

"""
## Problem Statement

Given a word (string) w, you need to find its next lexicographically greater permutation using exactly the same characters. In other words:
- If you imagine all the permutations (arrangements) of the letters in w sorted in dictionary order, you want to pick the smallest word that
  comes after w.
- If no such permutation exists (i.e. w is already the highest possible permutation), the answer is "no answer".

For example:
- For w = "ab", the only higher permutation is "ba".
- For w = "bb", every possible permutation is the same as w so answer is "no answer".
- For w = "hefg", the next highest is "hegf".
- For w = "dhck", the next highest is "dhkc".
- For w = "dkhc", the next highest is "hcdk".

---

## Solving Logic

The standard solution involves the well-known "next permutation" algorithm, which works by:

1. Identify the Pivot:
   Traverse the array (or string) from right to left to find the first character that is smaller than its next character.
   This character is called the pivot.

2. Find the Successor:
   Once the pivot is found, look again from the far right to locate the first character that is greater than the pivot.
   This is the character to swap with the pivot.

3. Swap Pivot and Successor:
   Swap these two characters. This slight increment ensures the new sequence is greater than the current one.

4. Reverse the Suffix:
   After the swap, the substring (or subarray) to the right of the pivot’s original index is in non-increasing (descending) order.
   Reverse this substring so that it becomes the lexicographically smallest (i.e. sorted in ascending order). This guarantees that
   the result is the immediate next greater permutation.

---

## Optimized Approach (Next Permutation Algorithm)

### Idea:

This method computes the next permutation in O(n) time (aside from the negligible cost of converting strings) without
generating all permutations. The steps are as follows:

1. Convert the String to a List:
   This is necessary in Python because strings are immutable.

2. Find the Pivot:
   Traverse the list from right to left to find the first index i where {arr}[i-1] < {arr}[i]. If not found, it means the string
   is in descending order (i.e. the highest permutation).

3. Find the Successor:
   Starting from the end, find the first element (at index j) that is greater than {arr}[i-1] (the pivot).

4. Swap the Pivot and Successor:
   Swap these two values.

5. Reverse the Suffix:
   Reverse the subarray starting from index i to the end. This step puts the tail into the smallest order to ensure we get the
   next immediate permutation.

6. Return the New Permutation:
   Convert the list back to a string and return it.
"""


# Time Complexity: O(n)
def biggerIsGreater(w):
    # Convert the string to a list for mutability.
    arr = list(w)
    n = len(arr)

    # 1. Identify the pivot: Traverse from right to left while the sequence is non-increasing.
    i = n - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1

    # If no pivot is found, then w is the highest permutation.
    if i <= 0:
        return "no answer"

    # 2. Find the rightmost successor to the pivot.
    j = n - 1
    while arr[j] <= arr[i - 1]:
        j -= 1

    # 3. Swap the pivot with the successor.
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # 4. Reverse the suffix starting from pivot's position to the end.
    arr[i:] = arr[i:][::-1]

    # Convert list back to string and return.
    return "".join(arr)


if __name__ == "__main__":
    print(biggerIsGreater("ab"))
    print(biggerIsGreater("bb"))
    print(biggerIsGreater("hefg"))


### Line-by-Line Explanation of the Optimized Code:
"""
- Line 2:  
  arr = list(w)  
  Convert the immutable string into a list to facilitate in-place modifications.

- Line 3:  
  n = len(arr)  
  Store the length of the list (number of characters). This is used throughout the algorithm.

- Lines 6–8:  
  python
  i = n - 1
  while i > 0 and arr[i - 1] >= arr[i]:
      i -= 1
    
  This loop scans from right to left to find the pivot—the first position where a character is less than the character 
  immediately after it. The loop stops when such a position is found or when the entire string is non-increasing. If no 
  pivot is found, it implies that w is the maximum permutation.

- Lines 10–11:  
  python
  if i <= 0:
      return "no answer"
    
  If the pivot wasn’t found (the loop reaches the start without breaking early), then there is no lexicographically 
  greater permutation, so return "no answer".

- Lines 14–16:  
  python
  j = n - 1
  while arr[j] <= arr[i - 1]:
      j -= 1
    
  This loop finds the rightmost character (the successor) that is greater than the pivot arr[i-1]. We start from the end 
  because the suffix is guaranteed to be in descending order.

- Line 19:  
  python
  arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
  Swap the pivot with the successor. This swap guarantees that the new string is higher than the original string.

- Line 22:  
  python
  arr[i:] = arr[i:][::-1]
    
  Reverse the subarray starting from the pivot's position to the end. Since that portion was in descending order, reversing 
  it puts it in ascending order, ensuring that the new permutation is the smallest lexicographically greater than the original.

- Line 25:  
  python
  return "".join(arr)
    
  Convert the list back into a string and return the result.
"""
