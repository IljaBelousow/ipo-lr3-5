x = int(input("Введите x: "))
y = int(input("Введите y: "))

if x == 0 and y == 0:
    print("Точка находится в начале координат")
elif x == 0:
    print("Точка лежит на оси Y")
elif y == 0:
    print("Точка лежит на оси X")
elif x > 0 and y > 0:
    print("Точка лежит в 1 четверти")
elif x < 0 and y > 0:
    print("Точка лежит во 2 четверти")
elif x < 0 and y < 0:
    print("Точка лежит в 3 четверти")
elif x > 0 and y < 0:
    print("Точка лежит в 4 четверти")
