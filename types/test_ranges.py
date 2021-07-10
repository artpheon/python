range1 = range(0, 10)
print(range1)
print(type(range1))
print(range1[5])
print(list(range1))
print(10 in range1)
print(range1.index(6)) #index of the value we are looking for

r1 = range(10, 100, 10)
print(r1.index(30))

r = range(3, 21)
my_slice = list(r)[6:9:]
print(my_slice)