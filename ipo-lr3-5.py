x = int(input("vvedite x "))
y = int(input("vvedite y "))
if x > 0 and y > 0:
    print("tochka lezhit v 1 chetverti")
elif x < 0 and y > 0:
    print("tochka lezhit vo 2 chetverti")
elif x < 0 and y < 0:
    print("tochka lezhit v 3 chetverti")
elif x > 0 and y < 0:
    print("tochka lezhit v 4 chetverti")
elif x == 0:
    print("tochka lezhit na osi")
elif y == 0:
    print("tochka lezhit na osi")
else:
    print("tochki netu :(")