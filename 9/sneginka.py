num = int(input("Введите число: "))
def func(num):
    if num > 0 and num % 2 != 0:
        for i in range(1, num + 1, 2):
            print(" " * ((num - i) // 2) + "*" * i)
        for i in range(num - 2, 0, -2):
            print(" " * ((num - i) // 2) + "*" * i)
    else:
        print("Введи еще раз")


r = func(num)







