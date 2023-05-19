# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

# First non-repeating character

def first_non_repeating_letter(s):
    s2 = s.lower()
    for i in s2:
        if s2.count(i) == 1:
            return s[s2.index(i)]

    return ''
