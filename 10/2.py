# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

# Stop gninnipS My sdroW!

def spin_words(sentence):
    new = ''
    for i in sentence.split():
        if len(i) >= 5:
            new += i[::-1] + " "
        else:
            new += i + " "
    return new.strip()