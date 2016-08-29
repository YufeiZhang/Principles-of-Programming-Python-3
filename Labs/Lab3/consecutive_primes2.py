# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.
#
# Written by Eric Martin


from math import sqrt


def is_not_prime(n):
    # Only used to test odd numbers.
    return any(n % d == 0 for d in range(3, round(sqrt(n)) + 1, 2))


print('The solutions are:\n')
# The list of all even i's such that a + i is one of a, b, c, d, e, f.
good_leaps = tuple(sum(range(0, k, 2)) for k in range(2, 13, 2))
for a in range(1001, 100000 - good_leaps[-1], 2):
    # i should be in good_leaps iff a + i is prime for i = 0, 2, 4, ..., 30.
    # Python does not have an operator for "A iff B",
    # but it has an operator for "A iff not B" (namely, ^), so we reformulate as:
    # i should be in good_leaps iff it is not true that a + i is not prime for i = 0, 2, 4, ..., 30.
    if all(((i in good_leaps) ^ is_not_prime(a + i)) for i in range(0, good_leaps[-1] + 1, 2)):
        for i in good_leaps[: -1]:
            print(a + i, end = '  ')
        print(a + good_leaps[-1])
