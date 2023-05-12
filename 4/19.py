# https://www.codewars.com/kata/58bf9bd943fadb2a980000a7/train/python

# Who is going to pay for the wall?

def who_is_paying(name):
    if len(name) <= 2:
        return [name]
    else:
        return [name, name[:2]]
