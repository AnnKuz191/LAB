w = ""
g = ""
i = 0
while w != "stop":
    w = str(input("Введите любое слово и нажмите Enter: "))
    g = g + " " + w
if w == "stop":
    gm = g.split()
    t = gm[:-1]
    it = ' '.join([str(elem) for elem in t])
print("Вот какая строка получилась: ", it)