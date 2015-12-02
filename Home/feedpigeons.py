"""
I start to feed one of the pigeons. A minute later two more fly by and a minute
after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food
lasts a pigeon for a minute, but in case there's not enough food for all the
birds, the pigeons who arrived first ate first. Pigeons are hungry animals and
eat without knowing when to stop. If I have N portions of bird feed, how many
pigeons will be fed with at least one portion of wheat?

Input: A quantity of portions wheat as a positive integer.
Output: The number of fed pigeons as an integer.
Precondition: 0 < N < 105.
"""

"""
Notes: The number of pigeons (and wheat being eaten) in each minute follows
the sequence of triangular numbers (https://oeis.org/A000217). So the number of
pigeons (and number of grains of wheat being eaten) in minute m are given by
    P = m(m + 1) / 2
    or:
    P = sum(x for x in range(m + 1)) - which is overkill given we have a formula
"""

def numPigeons(x):
    """Returns the number of pigeons present in the given minute"""
    return int(x * (x + 1) / 2)

def checkio(wheat):
    for minute in range(1, 105):
        if numPigeons(minute) < wheat:
            wheat -= numPigeons(minute)
            continue
        if numPigeons(minute) == wheat:
            return numPigeons(minute)
        if numPigeons(minute) > wheat:
            return max(numPigeons(minute - 1), wheat)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
