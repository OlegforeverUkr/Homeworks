# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

# Find The Parity Outlier

def find_outlier(integers):
    chet = []
    ne_chet = []
    for i in integers:
        if i % 2 == 0:
            chet.append(i)
        if i % 2 == 1:
            ne_chet.append(i)
    if len(chet) > len(ne_chet):
        return ne_chet[0]
    else:
        return chet[0]
