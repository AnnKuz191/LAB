colors=('красный','синий','жёлтый')

a, b = input("Первый цвет:"), input("Второй цвет:")
if a in colors and b in colors:
    if a != b:
        if (a in ('красный','синий')) and (b in ('красный','синий')):
            print('У вас получится фиолетовый')
        if (a in ('красный','жёлтый')) and (b in ('красный','жёлтый')):
            print('У вас получится оранжевый')
        if (a in ('синий','жёлтый')) and (b in ('синий','жёлтый')):
            print('У вас получится зелёный')
    else:
        print(a)
else:
    print("Ошибка цвета")
