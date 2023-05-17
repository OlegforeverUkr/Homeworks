# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

# Find the odd int
def find_it(seq):
    count = [x for x in seq if seq.count(x) % 2 == 1]
    return count[0]
