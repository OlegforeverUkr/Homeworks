# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python

# Remove duplicates from list

def distinct(seq):
    total = []
    for i in seq:
        if i not in total:
            total.append(i)
    return total
