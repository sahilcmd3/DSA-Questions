def missingNumbers(arr, brr):
    freq_arr = {}
    freq_brr = {}

    # Count frequencies in arr
    for num in arr:
        if num in freq_arr:
            freq_arr[num] += 1
        else:
            freq_arr[num] = 1

    # Count frequencies in brr
    for num in brr:
        if num in freq_brr:
            freq_brr[num] += 1
        else:
            freq_brr[num] = 1

    # Compare frequencies to find missing numbers
    result = []
    for num in freq_brr:
        if freq_brr[num] > freq_arr.get(num, 0):
            result.append(num)

    return sorted(result)


if __name__ == "__main__":
    print(missingNumbers(arr=[7, 2, 5, 3, 5, 3], brr=[7, 2, 5, 4, 6, 3, 5, 3]))
