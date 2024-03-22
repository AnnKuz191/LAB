def luckyNum():
    n = str(input("Введите номер: "))
    pr = len(n)
    if pr % 2 == 0:
        pol = len(n) // 2
        p1 = list(map(int, n[:pol]))
        p2 = list(map(int, n[pol:pr]))
        sump1 = sum(p1)
        sump2 = sum(p2)
        if sump1 == sump2:
            print(f"Вы ввели {n}, это - счастливый билет!")
        elif (sump1 -+ 1 == sump2) or (sump1 == sump2 -+ 1):
            print(f"Вы ввели {n}, этот билет к встрече))!")
        elif (sump1 -+ 2 == sump2) or (sump1 == sump2 -+ 2):
            print(f"Вы ввели {n}, это билет к пьянке! о.о")
        else:
            print(f"Вы ввели {n}, этот билет не счастливый!")
    else:
        print("Билет введён неправильно. Повторите попытку.")

luckyNum()
