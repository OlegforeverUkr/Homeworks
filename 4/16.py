# https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce/train/python

# Multiplication table for number

def multi_table(number):
    new_string = ''
    for i in range(1, 11):
        new_string += f'{i} * {number} = {i * number}\n'
    new_string = new_string[:-1]
    return new_string
