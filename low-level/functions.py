def print_hello():
    print("hello!")

print_hello()

def sum_mult(x, y, z):
    sum_xyz = (x + y) * z
    return sum_xyz
print(sum_mult(2, 3, 4))

def print_x_and_args(x, *args):
    print(x)
    for elem in args:
        print(elem)

print_x_and_args(5, 6, 7, 8, "new")

def do_something(x, **kwargs):
    print(x)
    print("Printing kwargs:")
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

do_something(5, elem = "ggg", lol = "lol", laf = "dfg")