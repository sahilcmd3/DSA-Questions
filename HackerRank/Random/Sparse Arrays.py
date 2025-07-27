"""There is a collection of input strings and a collection of query strings. For each query string, determine how
many times it occurs in the list of input strings. Return an array of the results."""


def sparse(stringList, queries):
    result = []

    for q in queries:
        result.append(stringList.count(q))

    return result


print(sparse(stringList=["aba", "baba", "aba", "xzxb"], queries=["aba", "xzxb", "ab"]))
