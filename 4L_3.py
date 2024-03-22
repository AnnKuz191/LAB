def magdat():
    d = input("Введите дату в формате: ДД.ММ.ГГГГ: ")
    data = d.split(".")
    if int(data[0]) * int(data[1]) == int(data[2][-2:]):
        print(True)
    else:
        print(False)

magdat()