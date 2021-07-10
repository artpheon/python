x = 0
while x < 10:
    x += 1
    print("x = ", x)

list1 = [10, 100, 1000]
list2 = [4, 5, 6]

for i in list1:
    for j in list2:
        print(i * j)

for num in range(100):
    if 55 <= num <= 66:
        print(num)

for num in range(100):
    if num > 50:
        break
    else:
        print(num)