from collections import defaultdict


def compute_next(x, y, n):
    # mask the last bit of x and y to be a zero
    top_left = x & ~(1 << n)
    bottom_left = y & ~(1 << n)

    # shift x and y by 1 to the right
    # (represents the next column)
    top_right = x >> 1
    bottom_right = y >> 1

    # we need exactly one of the four positions to contain a 1
    # and the rest need to be 0
    return (top_left & ~bottom_left & ~top_right & ~bottom_right) | \
        (~top_left & bottom_left & ~top_right & ~bottom_right) | \
        (~top_left & ~bottom_left & top_right & ~bottom_right) | \
        (~top_left & ~bottom_left & ~top_right & bottom_right)


def solution(g):
    cols = len(g)

    # transpose g
    g = list(map(list, zip(*g)))

    # turn map into a list of binary strings for each row of g
    g = [sum(has_gas * (1 << i) for i, has_gas in enumerate(row))
         for row in g]

    # dynamic programming to generate all possible
    # forward iterations of any state of the cellular
    # automaton on a given row (as a binary string)
    cache = defaultdict(set)
    g_rows = set(g)
    for left_row in range(1 << (cols + 1)):
        for right_row in range(1 << (cols + 1)):
            next_row = compute_next(left_row, right_row, cols)
            if next_row in g_rows:
                cache[next_row, left_row].add(right_row)

    # compute preimages of current rows and check
    # which ones align with preimages of the next rows
    preimage = {i: 1 for i in range(1 << (cols + 1))}
    for row in g:
        next_preimage = defaultdict(int)
        for left_row in preimage.keys():
            for right_row in cache[row, left_row]:
                next_preimage[right_row] += preimage[left_row]
        preimage = next_preimage

    # compute count of elements in preimage
    return sum(preimage.values())
