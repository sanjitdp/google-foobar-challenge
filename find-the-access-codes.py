# dynamic programming solution (O(n^2)):
# store number of previous elements dividing each
# element and simultaneously count triples
def solution(l):
    count_divisors = []

    triples = 0
    for i in range(len(l)):
        count = 0
        for j in range(i):
            # check if previous number divides current number
            # and if it does, increment our count of previous
            # divisors and add its previous divisors to the triples count
            if l[i] % l[j] == 0:
                count += 1
                triples += count_divisors[j]
        count_divisors.append(count)

    return triples
