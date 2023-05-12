# https://www.codewars.com/kata/586909e4c66d18dd1800009b/train/python

# Currying functions: multiply all elements in an array

def multiply_all(dumn):
    def multiply_All(n):
        return [i * n for i in dumn]

    return multiply_All

