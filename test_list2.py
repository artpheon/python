list1 = [1, 2, 3, 'a', 'b', 'c']
print("we got list: ", list1)
print(list1[0:3])
print(list1[2:5])
print(list1[2:])
print(list1[:])
print(list1[::2])
print(list1[1::2])

my_list = [22, 109, 'Apple', 11.2, 'Orange', 'Cherry', (10, 20, 30), [], False, 72, 'Kiwi', 0.0]
x = my_list[6:8]
print(x)

my_list = [10, 'x', 20.02, 'y', 30j, 'z', False]
my_list.append("Python 3")
print(my_list)

my_list = [10, 'x', 20.02, 'y', 30j, 'z', False]
my_list.pop(1)
print(my_list)

my_list = [10, -5, 20.02, 2018, 999]
my_list.sort()
print(my_list)