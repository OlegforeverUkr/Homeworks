# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

# Moving Zeros To The End

def move_zeros(lst):
    counter = 0
    for i in lst:
        if i == 0:
            counter += 1

    new_list = [i for i in lst if i != 0]
    ap = [0 for i in range(1, counter+1)]
    new_list.extend(ap)
    return new_list
