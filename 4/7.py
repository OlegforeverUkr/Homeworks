# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

# Removing Elements

def remove_every_other(my_list):
    new = []
    for id, i in enumerate(my_list):
        if id % 2 == 0:
            new.append(i)
    return new