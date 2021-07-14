myfile = open("myfile.txt", "w")

myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

myfile.close()

myfile = open("myfile.txt")

#This should return "Javascript\n"
print(myfile.readlines()[2])

myfile = open("myfile2.txt", 'w+')

myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift")

myfile.seek(0)

#This should return "Javascript"
print(myfile.readlines()[2])
myfile.close()


myfile = open("myfile2.txt", "w")

myfile.write("Python\nJava\nJavascript\nC++\nHTML\nCSS\nSwift\n")

myfile.close()

myfile = open("myfile2.txt", 'a+')

myfile.write("Ruby")

myfile.seek(0)

#This should return "Ruby"
print(myfile.readlines()[7])