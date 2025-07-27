# Grading Students


def gradStu(grades):
    result = []

    for grade in grades:
        if grade >= 38:
            # Next multiple of 5
            next = ((grade // 5) + 1) * 5
            # If difference is less than 3
            if next - grade < 3:
                result.append(next)
            else:
                result.append(grade)
        # No rounding for grades below 38
        else:
            result.append(grade)

    return result


print(gradStu(grades=[73, 67, 38, 33]))
