"""
 You are given a text, which contains different english letters and punctuation
 symbols. You should find the most frequent letter in the text. The letter
 returned must be in lower case. While checking for the most wanted letter,
 casing does not matter, so for the purpose of your search, "A" == "a". Make
 sure you do not count punctuation symbols, digits and whitespaces, only
 letters.

If you have two or more letters with the same frequency, then return the letter
which comes first in the latin alphabet. For example -- "one" contains "o", "n",
"e" only once for each, thus we choose "e".

Input: A text for analysis as a string (unicode for py2.7).

Output: The most frequent letter in lower case as a string.

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 10^5
"""

def checkio(text):
    import string
    text = text.lower()
    recordLetter, recordCount = '', 0
    for letter in string.ascii_lowercase:
        letterCount = text.count(letter)
        if letterCount > recordCount:
            recordLetter, recordCount = letter, letterCount
    return recordLetter


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

"""
bryukh's solution:
import string
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
"""
