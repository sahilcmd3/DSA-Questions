# HackerRank beautiful days at the movies

def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j + 1):
        rev = int(str(day)[::-1])
        if abs(day - rev) % k == 0:
            count += 1
    return count


if __name__ == "__main__":
    print(beautifulDays(i=20, j=23, k=6))
