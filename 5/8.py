# https://www.codewars.com/kata/582ba36cc1901399a70005fc/train/python

# Coding Meetup #11 - Higher-Order Functions Series - Find the average age

def get_average(lst):
    age = []
    for i in lst:
        age.append(i.setdefault("age"))
    return round(sum(age)/len(age))
