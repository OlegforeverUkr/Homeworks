x = input("Insert first value - ")
y = input("Insert second value - ")
z = input("Choise dict or list? (d\l)- ").lower()


def make_dict(a, b):
    new_dict = {}
    a = "".join(a.split())
    b = "".join(b.split())
    shorts = len(sorted((a, b), key=len)[0])
    for i in range(shorts):
        new_dict[a[i]] = b[i]
    return new_dict


def make_list(a, b):
    new_list = []
    a = "".join(a.split())
    b = "".join(b.split())
    shorts = len(sorted((a, b), key=len)[0])
    for i in range(shorts):
        new_list.append(f'{a[i]}{b[i]}')
    return new_list


if z == 'd':
    print(make_dict(x, y))
elif z == 'l':
    print(make_list(x, y))
else:
    print('Insert carrect data!!!')
