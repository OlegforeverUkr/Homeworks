# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

# Array.diff

def array_diff(a, b):
    answ = []
    if not b:
        return a
    for i in a:
        if i not in b:
            answ.append(i)

    return answ

