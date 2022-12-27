from functools import reduce
import operator

# returns the product of elements in an iterable


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def solution(xs):
    # if we have no choice, return the only element
    if len(xs) == 1:
        return str(xs[0])

    # filter for negative elements and positive elements,
    # sort list of negative elements since at most 50 element input
    positive_elements = list(filter(lambda x: x > 0, xs))
    negative_elements = sorted(list(filter(lambda x: x < 0, xs)))

    # generate maximum positive and negative product,
    # since all inputs are integers
    prod_positive = prod(positive_elements)
    prod_negative = prod(negative_elements) if len(
        negative_elements) % 2 == 0 else prod(negative_elements[:-1])

    # if we can only make a negative product or zero, return zero
    # here, list length is larger than 1 so there must be a zero
    if not positive_elements and len(negative_elements) == 1:
        return "0"

    # in all other cases, return max neg product * max pos product
    # since all inputs are integers
    else:
        return str(prod_positive * prod_negative)
