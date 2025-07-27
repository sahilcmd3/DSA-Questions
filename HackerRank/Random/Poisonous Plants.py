def poisonousPlants(p):
    stack = []
    max_days = 0

    for pesticide in p:
        days = 0
        while stack and pesticide <= stack[-1][0]:
            days = max(days, stack.pop()[1])
        if not stack:
            days = 0
        else:
            days += 1
        max_days = max(max_days, days)
        stack.append((pesticide, days))

    return max_days