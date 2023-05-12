summa = int(input("Insert summu - "))
kupyri = [10, 20, 50, 100, 200, 500, 1000]
po_1000 = 0
po_500 = 0

for id, i in enumerate(kupyri):
    k = summa / i

    if summa > 18800:
        print("Невозможно выдать эту сумму!!!")
        break
    if summa > 3800:
        while summa > 3800:
            if po_500 < 10:
                summa -= 500
                po_500 += 1
            else:
                summa -= 1000
                po_1000 += 1

    if 360 > summa > 100 and k > 10:
        if (summa - 10 * i) % kupyri[id + 1] == 0:
            summa -= 10 * i
            print(f'Купюр номиналом {i} - 10')
            continue
        if (summa + i) % kupyri[id + 1] == 0:
            summa -= 9 * i
            print(f'Купюр номиналом {i} - 9')
            continue
        if (summa + 2 * i) % kupyri[id + 1] == 0:
            summa -= 8 * i
            print(f'Купюр номиналом {i} - 8')
            continue
        if (summa + 3 * i) % kupyri[id + 1] == 0:
            summa -= 7 * i
            print(f'Купюр номиналом {i} - 7')
            continue
        if (summa + 4 * i) % kupyri[id + 1] == 0:
            summa -= 6 * i
            print(f'Купюр номиналом {i} - 6')
            continue
        if (summa + 5 * i) % kupyri[id + 1] == 0:
            summa -= 5 * i
            print(f'Купюр номиналом {i} - 5')
            continue

    if summa < 100 and summa != 0:
        summa -= k * i
        print(f'Купюр номиналом {i} - {int(k)}')
        continue


    if k > 10:
        k = 10
        if (summa - 10 * i) % kupyri[id + 1] == 0:
            summa -= 10 * i
            print(f'Купюр номиналом {i} - 10')
            continue
        elif (summa / kupyri[id + 1]) >= 10:
            if summa % kupyri[id + 1] == 0:
                summa -= 10 * i
                print(f'Купюр номиналом {i} - 10')
                continue
            elif (summa + i * 10) % kupyri[id + 1] == 0 and (summa + i * 10) % kupyri[id + 2] == 0:
                summa -= k * i
                print(f'Купюр номиналом {i} - 10')
                continue
            elif (summa + i) % kupyri[id + 1] == 0 and (summa + i) % kupyri[id + 2] == 0:
                summa -= 9 * i
                print(f'Купюр номиналом {i} - 9')
                continue
            elif (summa + i * 2) % kupyri[id + 1] == 0 and (summa + i * 2) % kupyri[id + 2] == 0:
                summa -= 8 * i
                print(f'Купюр номиналом {i} - 8')
                continue
            elif (summa + i * 3) % kupyri[id + 1] == 0 and (summa + i * 3) % kupyri[id + 2] == 0:
                summa -= 7 * i
                print(f'Купюр номиналом {i} - 7')
                continue
            elif (summa + i * 4) % kupyri[id + 1] == 0 and (summa + i * 4) % kupyri[id + 2] == 0:
                summa -= 6 * i
                print(f'Купюр номиналом {i} - 6')
                continue
            if ((summa - i * 10) / kupyri[id + 1]) >= 10:
                summa -= 10 * i
                print(f'Купюр номиналом {i} - 10')
                continue


        else:
            if (summa + i) % kupyri[id + 1] == 0:
                summa -= 9 * i
                print(f'Купюр номиналом {i} - 9')
                continue
            if (summa + 2 * i) % kupyri[id + 1] == 0:
                summa -= 8 * i
                print(f'Купюр номиналом {i} - 8')
                continue
            if (summa + 3 * i) % kupyri[id + 1] == 0:
                summa -= 7 * i
                print(f'Купюр номиналом {i} - 7')
                continue
            if (summa + 4 * i) % kupyri[id + 1] == 0:
                summa -= 6 * i
                print(f'Купюр номиналом {i} - 6')
                continue
            if (summa + 5 * i) % kupyri[id + 1] == 0:
                summa -= 5 * i
                print(f'Купюр номиналом {i} - 5')
                continue

    elif k <= 10 and summa != 0:
        summa -= k * i
        print(f'Купюр номиналом {i} - {int(k)}')

    if summa == 0:
        if po_500 > 0:
            print(f'Купюр номиналом 500- {po_500}')
        if po_1000 > 0:
            print(f'Купюр номиналом 1000 - {po_1000}')
        break
