# https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python

# Return Two Highest Values in List

def two_highest(arg1):
    new_list = sorted([i for i in arg1], reverse=True)
    new_list2 = []
    for i in new_list:
        if i not in new_list2:
            new_list2.append(i)
    return new_list2[:2]


r = two_highest([15, 20, 20, 17])
print(r)
