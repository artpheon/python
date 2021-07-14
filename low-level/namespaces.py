myVariable= 5

def printVariable():
    global myVariable
    print(myVariable)

print(list(range(10)))
printVariable()