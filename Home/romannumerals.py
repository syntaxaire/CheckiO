"""
Roman numerals come from the ancient Roman numbering system. They are based on
specific letters of the alphabet which are combined to signify the sum (or, in
some cases, the difference) of their values. The first ten Roman numerals are:
I, II, III, IV, V, VI, VII, VIII, IX, and X.
The Roman numeral system is decimal based but not directly positional and does
not include a zero. Roman numerals are based on combinations of these seven
symbols:
Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia
article. For this task, you should return a roman numeral using the specified
integer value ranging from 1 to 3999.

Input: A number as an integer.
Output: The Roman numeral as a string.
Precondition: 0 < number < 4000
"""

def checkio(number, result = '', romans = None):
    if romans == None:
        romans = [[1, 'I'], [4, 'IV'], [5, 'V'], [9, 'IX'], [10, 'X'],
                 [40, 'XL'], [50, 'L'], [90, 'XC'], [100, 'C'], [400, 'CD'],
                 [500, 'D'], [900, 'CM'], [1000, 'M']]
    while number >= romans[-1][0]:
        result += romans[-1][1]
        number -= romans[-1][0]
    if number == 0:
        return result
    print("Number currently {}, result currently {}, popping {}".format(number, result, romans[-1][0]))
    romans.pop()
    return checkio(number, result, romans)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
