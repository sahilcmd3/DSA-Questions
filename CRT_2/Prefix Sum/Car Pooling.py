# LEETCODE 1094

"""There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, from i, to i] indicates that the ith
trip has numPassengersi passengers and the locations to pick them up and drop them off are from i and to i respectively. The
locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise."""


# Time Complexity: O(N+M)
def carPool(trips, capacity):
    max_distance = max(trip[2] for trip in trips)
    diff_array = [0] * (max_distance + 1)

    for numPassengers, start, end in trips:
        diff_array[start] += numPassengers
        diff_array[end] -= numPassengers

    currentPassengers = 0
    for passengers in diff_array:
        currentPassengers += passengers
        if currentPassengers > capacity:
            return False

    return True


if __name__ == "__main__":
    print(carPool(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))



"""Difference array ek powerful technique hai jo kisi array me efficient range updates karne ke liye use hoti hai. 
Yeh prefix sum ka ek variation hai, lekin yeh updates ko **incremental way** me store karta hai.

### Difference Array Ka Basic Concept
1. Ek normal array me agar hume kisi range ([L, R]) me +X karna ho, toh hume har index par manually increment karna padta hai.
2. Difference array approach me sirf do jagah pe updates karte hain:
   - `diff[L] += X` (L par X add karo)
   - `diff[R + 1] -= X` (R ke baad X subtract karo)

Baad me ek prefix sum lagane se actual values milti hain.

---

### Car Pooling Problem (LeetCode 1094) Me Difference Array
Is problem me hume passengers ki entry aur exit track karni hoti hai. Difference array approach isko efficiently solve karti hai.

#### Step-by-step approach
1. Ek difference array `diff` banate hain jo initially 0 hoti hai.
2. Har trip ke liye:
   - `diff[start] += numPassengers` (Yahan passengers enter ho rahe hain)
   - `diff[end] -= numPassengers` (Yahan passengers utar rahe hain)
3. Prefix sum lagakar har jagah pe total passengers nikalte hain.
4. Agar kahin pe capacity exceed ho jaye, toh return False.

---

### Kyu Use Kare Difference Array?
Brute force se fast hai, kyunki har trip ke liye har index update nahi karna padta.  
Space efficient hai, kyunki sirf necessary points par change hota hai.  
Range updates me best hai, kyunki ek hi loop me solution aa jata hai."""
