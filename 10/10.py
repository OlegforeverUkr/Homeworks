# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python

# Simple Pig Latin

def pig_it(text):
    new = ''
    for i in text.split():
        if i != "!" and i != "?":
            new += f'{i[1:]}{i[0]}ay '
        else:
            new += i
    return new.strip()

