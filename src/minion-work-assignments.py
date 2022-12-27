from collections import Counter


def solution(data, n):
    # create dictionary of item counts
    counts = Counter(data)

    # filter for items with count at most n
    return list(filter(lambda x: counts[x] <= n, data))
