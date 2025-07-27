#LEETCODE (medium)

"""Given an array of integers citations where citations[i] is the number of citations a researcher received for their
ith paper, return the researcher's h-index.

The h-index is an author-level metric that measures both the productivity and citation impact of the publications,

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that
the given researcher has published at least h papers that have each been cited at least h times."""

#Time Complexity: O(NLogN)
def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

# Example usage
citations = [3, 0, 6, 1, 5]
print(hIndex(citations))  # Output: 3