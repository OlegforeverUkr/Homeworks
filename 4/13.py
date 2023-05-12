# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python

# The Feast of Many Beasts

def feast(beast, dish):
    if dish[-1] == beast[-1] and dish[0] == beast[0]:
        return True
    else:
        return False
