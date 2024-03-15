import random

osh=0
pr = 0

while osh < 3:

    a = random.randint(0, 10)
    b = random.randint(0, 10)

    s = a + b

    print("Ввведите ответ на это выажение: ", a, "+", b, "= ", end="")
    summa = int(input())

    if s == summa:
        print("Правильно!")
        pr += 1
    else:
        print("Ответ неверный!")
        osh += 1

if osh == 3:
    print("Игра окончена. Правильных ответов: ", pr)


