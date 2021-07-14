myfile = open("file.txt", "r")
print("File was opened with mode: " + myfile.mode)
print(myfile.read())
print('We have read the whole file and now we are on position: ' + str(myfile.tell()))
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
string1 = myfile.readline()

print('The string we got from readline: ' + string1)
myfile.seek(0)

for line in myfile.readlines():
    if (line.startswith('c')):
        print(line)