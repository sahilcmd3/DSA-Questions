# LEETCODE 1109

"""There are n flights that are labeled from 1 to n.
You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights first 
i through lasti (inclusive) with seatsi seats reserved for each flight in the range.
Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.
"""

# Difference Array Technique
# Instead of updating all flights in the range first_i to last_i, we:
# Add seats_i at first_i - 1
# Subtract seats_i at last_i (to cancel after the range) Then compute prefix sums to get final seat reservations.



# Time Complexity: O(m + n) where m is number of bookings
# Space Complexity: O(n)
def coporate(bookings, n):
    result = [0] * n
    # For each booking [first, last, seats]:
    # - Add seats at position (first - 1)
    # - Subtract seats at position (last) if within bounds
    for first, last, seats in bookings:
        result[first - 1] += seats  # Convert to 0 based indexing
        if last < n:  # Only subtract when within bounds
            result[last] -= seats

    # Convert difference array to actual values using prefix sum
    for i in range(1, n):
        result[i] += result[i - 1]

    return result


if __name__ == "__main__":
    bookings1 = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n1 = 5
    print(f"Input: bookings = {bookings1}, n = {n1}")
    print(f"Output: {coporate(bookings1, n1)}")
