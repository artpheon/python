list1 = [1, 2 , 3, 4, 5, 2, 3]
print(set(list1))
set1 = {4, 5, 11, 12, 13, 14, 14, 15}
print(set1)
print(1 in set1, 2 in set1, 15 in set1)
set2 = set(list1)
print("Intersection of 2 sets: ", set1.intersection(set2))
print("Differences of 2 sets: ", set1.difference(set2))


list1 = [1,2,3,4]
list2 = [3,4,7]

fs1 = frozenset(list1)
fs2 = frozenset(list2)
print(fs1, fs2)

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1.add(500)
set1.remove(7)
print(set1)

set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set4 = {2, 4, 6, 9}
print(set3.difference(set4))

set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 19}

set6 = {0, 2, 4, 6, 9, 11, 14}

x = set5.intersection(set6)

print(x)