"""
We need a solution which can pass any case. The result of your solution should
pass for any comparison with anything.

You should write the function "checkio" which is called with one argument, the
result will be compared with some other data (==, !=, etc) and the result of
that comparison should be True.

Input: Some data. Maybe that data over there.

Output: The something as a something-else.

Example:
checkio({}) != [] # True
checkio('Hello') < 'World' # True
checkio(80) > 81 # True
checkio(re) >= re # True
checkio(re) <= math # True
checkio(5) == ord # True

How it is used: This task will show you how to use Python "magic".
"""

# Inspired by KenMercusLai's solution
class soothsayer:
    def __init__(self, thing): pass
    def sooth(self, anotherthing): return True
    __lt__, __gt__, __ge__, __le__, __eq__, __ne__ = sooth, sooth, sooth, sooth, sooth, sooth


def checkio(anything):
    return soothsayer(anything)


if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],         'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')
