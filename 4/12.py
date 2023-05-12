# https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python

# Add Length
def add_length(str_):
    new = []
    for i in str_.split():
        new.append(f'{i} {len(i)}')
    return new
