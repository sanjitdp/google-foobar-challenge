from math import factorial
from collections import Counter

# computes the gcd of a and b
# using the Euclidean algorithm


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# use multinomial coefficient to compute
# number of cycles with the given partition sizes


def count_cycles(partitons, n):
    total = factorial(n)
    for cycle_number, cycle_size in Counter(partitons).items():
        total /= (cycle_number ** cycle_size) * factorial(cycle_size)
    return total

# count the number of partitions of n + i elements
# split into groups of n and i, using dynamic programming


def cycle_partitions(n, i=1):
    yield [n]
    for i in range(i, n//2 + 1):
        for p in cycle_partitions(n-i, i):
            yield [i] + p

# use Burnside's lemma to compute the size of
# (Z/s)^(w * h) / (S_w * S_h)


def solution(w, h, s):
    total = 0
    for partition_w in cycle_partitions(w):
        for partition_h in cycle_partitions(h):
            m = count_cycles(partition_w, w) * count_cycles(partition_h, h)
            total += m * \
                (s ** sum([sum([gcd(i, j) for i in partition_w])
                 for j in partition_h]))

    return str(int(total / (factorial(w) * factorial(h))))
