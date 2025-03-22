#LEETCODE (medium)

"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);"""

#Time Complexity: O(n)
def convert(s, numRows):
    if numRows == 1 or numRows >= len(
            s):  #If numRows is 1 or greater than or equal to the length of the input string s,
        # it means that the ZigZag pattern will be the same as the input string. In such cases, just return the input
        # string s as it is
        return s

    idx, d = 0, 1  #Initialize idx to keep track of the current row index, starting from 0, and d as the direction
    # of traversal (1 for downward, -1 for upward).
    rows = [[] for _ in
            range(numRows)]  #Create a list of numRows empty lists to represent the rows of the ZigZag pattern.

    for char in s:
        rows[idx].append(char)
        if idx == 0:
            d = 1  #Update the direction d based on the current position (idx).
        elif idx == numRows - 1:
            d = -1
        idx += d  #Update the current row index idx according to the direction d.

    for i in range(numRows):
        rows[i] = ''.join(rows[i])  #Join the characters in each row to form strings
        # Update each row in rows with the joined string.

    return ''.join(rows)  #Join all the rows together to form the final ZigZag pattern


s = "PAYPALISHIRING"
numRows = 3
ans = convert(s, numRows)
print(ans)