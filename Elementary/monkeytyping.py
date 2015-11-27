"""
 The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite length of time will almost surely type out a given text, such as the complete works of John Wallis, or more likely, a Dan Brown novel.

Let's suppose our monkeys are typing, typing and typing, and have produced a wide variety of short text segments. Let's try to check them for sensible word inclusions.

You are given some text potentially including sensible words. You should count how many words are included in the given text. A word should be whole and may be a part of other word. Text letter case does not matter. Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once.

For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).

Output: The number of words in the text as an integer.

Precondition:
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words) """

def count_words(text, words):
    matchcount = 0
    for word in words:
        if word in text.lower:
            matchcount += 1
    return matchcount
