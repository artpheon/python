from itertools import *
list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']

chained = chain(list1, list2)
print(type(chained))
print(list(chained))

counter = count(10, 2.5)

for i in counter:
    if i <= 20:
        print(i)
    else:
        break

newRange = range(0, 5)
newCycle = cycle(newRange)

ex = 0
for i in newCycle:
    print(i)
    ex += 1
    if (ex == 20):
        break

res = list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8]))
print(res)


r1 = range(1,21)
my_list = list(islice(r1, 6, 16, 2))
print(my_list)