# https://www.codewars.com/kata/583952fbc23341c7180002fd/train/python

# Coding Meetup #14 - Higher-Order Functions Series - Order the food

def order_food(lst):
    answer = {}
    for i in lst:
        count = 0
        if i.get("meal") not in answer:
            count += 1
            answer[i.setdefault("meal")] = count
        else:
            answer[i.setdefault("meal")] += 1
    return answer
