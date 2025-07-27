# LEETCODE 2073


def timeRequired(tickets, k):
    n = len(tickets)
    i = -1
    time = 0
    
    while tickets[k] != 0:
        i += 1
        if i == n:
            i = 0
        if tickets[i] > 0:
            tickets[i] -= 1
        else:
            continue

        time += 1
    
    return time


if __name__ == "__main__":
    print(timeRequired(tickets=[2, 3, 2], k=2))
