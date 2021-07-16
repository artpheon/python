a = lambda x, y: x * y
b = lambda x: x + 10
c = lambda x, y: print(x + y)

testList1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
d = lambda x: x[1]
testList1.sort(key = d)
testList1.sort(key = lambda x: x[1])
print(testList1)
c(10, 5)

listOfDicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
listOfDicts.sort(key = lambda x: int(x.get('model', '0')), reverse = True)
print(listOfDicts)

mapped = list(map(lambda x: x * 10, range(10)))
print(mapped)
filtered = list(filter(lambda y: y > 5, range(10)))
print(filtered)