#https://www.codewars.com/kata/5a07e5b7ffe75fd049000051

#Sort My Textbooks

def sorter(textbooks):
    b = sorted(textbooks, key=str.lower)
    return b


d = sorter(['Algebra', 'history', 'Geometry', 'english'])
print(d)
