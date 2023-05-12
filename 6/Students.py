students = {
    "Иванов Петр": ["Python", "FrontEnd", "Java"],
    "Сидоров Иван": ["FullStack", "Java"],
    "Петров Алексей": ["FrontEnd"],
    "Смирнова Елена": ["Python"],
    "Кузнецова Ольга": ["FrontEnd", "Java"],
    "Васильев Дмитрий": ["Python", "FullStack"],
    "Морозов Сергей": ["Java"],
    "Николаева Анна": ["Python", "FullStack"],
    "Павлов Денис": ["FrontEnd"],
    "Козлов Игорь": ["Python"],
}


def more_than_two(l):
    students_more_than_two = [i for i, x in l.items() if len(x) >= 2]
    return ',\n'.join(students_more_than_two)


#
def without_front_end(l):
    students_not_frontend = [i for i, x in l.items() if "FrontEnd" not in x]
    return ',\n'.join(students_not_frontend)


#
def python_java(l):
    students_python_java = [i for i, x in l.items() if "Python" in x or "Java" in x]
    return ',\n'.join(students_python_java)


print(python_java(students))
