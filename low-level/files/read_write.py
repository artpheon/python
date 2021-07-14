newFile = open('newfile.txt', 'w')
chars = newFile.write("Adding some new text\nhere.\n")
print("Created a file and wrote a tring of length ", str(chars), " to it.")
try:
    newFile.read()
except:
    print("Could not read from file")
newFile.close()
newFile = open('newfile.txt', 'w')
newFile.writelines(['First', 'Second', 'Third'])
newFile.close()
newFile = open('newfile.txt', 'a')
newFile.writelines(['These', 'Strings', 'Were', 'Appended'])
newFile.close()