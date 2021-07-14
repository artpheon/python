with open('to_remove.txt', 'r+') as file:
    file.write('Python is the greatest language')
    file.seek(0)
    print(file.read())
    leftChars = file.truncate(10)
    print('Left: ', leftChars, ' chars in the file')
print(file)
print(type(file))