# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

# Count of positives / sum of negatives

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    positive = len([1 for i in arr if i > 0])
    summa = sum([i for i in arr if i < 0])

    return [positive, summa]
