# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

# Sum of Digits / Digital Root
def digital_root(n):
    answer = 0
    while n > 9:
        for i in str(n):
            answer += int(i)
        n = answer
        answer = 0
    return n
