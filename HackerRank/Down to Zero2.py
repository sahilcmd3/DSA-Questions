from collections import deque


def downtozero(n):
    a = len(n)
    visited = [False] * (a + 1)
    queue = deque([(a, 0)])

    while queue:
        current, steps = queue.popleft()
        if current == 0:
            return steps
        if visited[current]:
            continue

        visited[current] = True

        queue.append((current - 1, steps + 1))

        for i in range(2, int(current**0.5) + 1):
            if current % i == 0:
                queue.append((max(i, current // i), steps + 1))


if __name__ == "__main__":
    print(downtozero(n=[2, 3, 4]))
