sl = ""

while sl != "stop":
    sl = str(input("Введите слово: "))
    if sl != "stop":
        if "ф" in sl:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
    else:
        break