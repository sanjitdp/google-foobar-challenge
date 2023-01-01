# truncated digits of sqrt(2)
truncated_digits = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

# multiply the truncated part by n and shift accordingly


def truncated_multiply(n):
    return (truncated_digits * n) // (10 ** 100)

# solve using a recurrence relation


def solve(n):
    # base case
    if n <= 1:
        return n == 1
    else:
        return n * truncated_multiply(n) + n * (n + 1) / 2 - truncated_multiply(n) * (truncated_multiply(n) + 1) / 2 - solve(truncated_multiply(n))

# return answer as a string


def solution(n):
    n = int(n)
    return str(solve(n))
