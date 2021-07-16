list1 = []
for i in range(10):
    result = 2 ** i
    list1.append(result)
print(list1)

#another way to do this:

list2 = [2 ** x for x in range(10)]
print(list2)

list3 = [2 ** x for x in range(10) if x > 5]
print(list3)

dict1 = {x : 2 ** x for x in range(10)}
print(type(dict1))
for key in dict1:
    print(key,": ", dict1[key])

print([x * 10 for x in range(1, 11) if x > 7])