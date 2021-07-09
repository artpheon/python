list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
print(list1)
print("Size of list1: " + str(len(list1)))
print("First element is %s" % list1[0])
list1[2] = "HP"
print("New list: ", list1)
list1.append(100)
del list1[4]
print(list1)
list1.pop(4)
list1.remove(100)
list1.insert(0, "First element")
print(list1)
print(list1[len(list1) - 1])
print(list1[-1])

list2 = [354, 645, 14, 76, 2, 54, 986]
print("List2: ", list2)
list2.sort()
print("List2 sorted: ", list2)
list2.reverse()
print("List2 sorted in reverse: ", list2)
