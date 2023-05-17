# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

# Counting Duplicates

def duplicate_count(text):
    text = text.lower()
    counter = 0
    for i in text:
        if text.count(i) > 1:
            counter += 1
            text = text.replace(i, "")
    return counter
