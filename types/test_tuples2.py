# tuples - immutable()
# lists - mutable[]

a = ()
b = []
print(type(a))
print(type(b))
print(dir(a), '\n')
print(dir(b))

tuple1 = (1,2,3,4,5,6)
print("Tuple1: ", tuple1)
print("Is 10 in tuple1?", 10 in tuple1)
print(tuple1[::-1])
print(tuple1[1::2])
print(tuple1[::2])
