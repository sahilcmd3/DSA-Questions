# There is a collection of input strings and a collection of query strings. For each query string, determine how many
# times it occurs in the list of input strings. Return an array of the results.


def matchingStrings(strings, queries):
    result = []

    for query in queries:
        result.append(strings.count(query))

    return result


if __name__ == "__main__":
    print(
        matchingStrings(
            strings=["aba", "baba", "aba", "xzxb"], queries=["aba", "xzxb", "ab"]
        )
    )
