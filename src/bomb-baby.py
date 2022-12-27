# solve using backward induction on (x, y)
def solution(x, y):
    # convert x, y to numeric type
    a = int(x)
    b = int(y)

    # make sure a <= b by symmetry of the problem
    if a > b:
        a, b = b, a

    # count number of steps
    count = 0

    # start computing what must have happened in the past
    # to arrive at the goal numbers
    while a >= 1 and b >= 1:
        # check if we arrived at the starting state
        if a == 1 and b == 1:
            return str(count)

        # check whether a divides b
        if b % a == 0:
            if a == 1:
                return str(count + b - 1)
            else:
                return "impossible"

        # we must have added a to b in the previous few steps,
        times_added = b // a
        b = b % a

        # ensure that a <= b due to symmetry of the problem
        a, b = b, a

        # add to counter
        count += times_added

    # one of the numbers is now less than 1, so impossible
    return "impossible"
