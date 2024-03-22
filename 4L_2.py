def prgdel():
    try:
        b = int(input("Введите число: "))
        pr = 100 / b
        print (f"Вы ввели {b}, ответ: {pr}")
    except (ValueError):
        print ("Неправильный ввод, вы добавили буквы. Попробуйте еще раз.")
    except (ZeroDivisionError):
        print ('Ошибка! Деление на 0.')

prgdel()