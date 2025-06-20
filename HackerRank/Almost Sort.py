# HackerRank -> Almost Sorted

# Time Complexity: O(n)
def almostSorted(arr):
    sorted_arr = sorted(arr)

    diff = [i for i in range(len(arr)) if arr[i] != sorted_arr[i]]

    if not diff:
        print("yes")
    elif len(diff) == 2:
        print("yes")
        print(f"swap {diff[0]+1} {diff[1]+1}")
    else:
        l = diff[0]
        r = diff[-1]
        if arr[l : r + 1] == sorted_arr[l : r + 1][::-1]:
            print("yes")
            print(f"reverse {l+1} {r+1}")
        else:
            print("no")


if __name__ == "__main__":
    print(almostSorted(arr=[3, 1, 2]))
