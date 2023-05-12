# https://www.codewars.com/kata/57fae964d80daa229d000126/train/python

# Exclamation marks series #1: Remove an exclamation mark from the end of string


def remove(s):
    if s == "":
        return s
    elif s[-1] == "!":
        return s[:-1]
    else:
        return s
