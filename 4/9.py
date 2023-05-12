# https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/train/python

# My head is at the wrong end!
def fix_the_meerkat(arr):
    arr[-1], arr[0] = arr[0], arr[-1]
    return arr
