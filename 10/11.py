# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

# Scramblies

def scramble(str1, str2):
    slov = {}
    for i in str1:
        slov[i] = slov.get(i, 0) + 1

    for x in str2:
        if x not in slov or slov[x] == 0:
            return False
        slov[x] -= 1

    return True

r = scramble("cedewaraaossoqqyt", "codewars")
print(r)
