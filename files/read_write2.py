newFile = open('newtxtrandomfile.txt', 'w+')
newFile.write('Writing a random line')
newFile.close()
print("NewFile closed?", newFile.closed)

print('Another way of opening/closing a file:')
with open("here.txt", 'w+') as f:
    f.write("Wrote a line inside a file")
    f.seek(0)
    print(f.read())
print("f is closed? ", f.closed)