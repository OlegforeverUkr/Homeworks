students = {"Vasya": [1, 2, 3, 4],
            "Petya": [2, 3, 3, 5],
            "Illya": [5, 5, 5, 5, 2, 2, 2],
            "Nadya": [2, 3, 3, 4, 1],
            "Gulya": [5, 3, 3, 5, 3]}


def min_max(x):
    new = []

    for i in x.values():
        middle = 0
        for c in i:
            middle += c
        new.append(middle / len(i))
    list_students = [i for i in x.keys()]
    worst = list_students[new.index(min(new))]
    best = list_students[new.index(max(new))]

    return f'Worst in class - {worst}\nBest in class - {best}'


print(min_max(students))