myList = [6, 23, 7, 2, 1, 7, 0, 54]
myIterator = iter(myList)
print(myIterator)

for elem in myList:
    print(elem)

for i in range(8):
    i = i + 1
    print(next(myIterator))


def myGenerator(x:int, y:int):
    for i in range(x):
        print("i = %d" % i)
        print("y = %d" % y)
        yield y * i

genObject = myGenerator(10, 6)
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))
print(next(genObject))

gen_exp = (x for x in range(5))

print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))