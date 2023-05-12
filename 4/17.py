# https://www.codewars.com/kata/596fba44963025c878000039/train/python

# Contamination #1 -String-

def contamination(text, char):
    if not text or not char:
        return ""
    else:
        return str(len(text) * char)
