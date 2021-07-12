fig = str(input())
if fig == "треугольник":
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    halfP = (side3 + side2 + side1) / 2
    print((halfP * (halfP - side1) * (halfP - side2) * (halfP - side3)) ** 0.5)
elif fig == "прямоугольник":
    side1 = float(input())
    side2 = float(input())
    print(side1 * side2)
elif fig == "круг":
    rad = float(input())
    print(3.14 * (rad ** 2))
else:
    print("Неизвестная фигура!")