def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "No"

    return "Yes"


if __name__ == "__main__":
    print(twoArrays(k=1, A=[0, 1], B=[0, 2]))
