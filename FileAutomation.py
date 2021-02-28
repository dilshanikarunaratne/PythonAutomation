import os

#specify the path of the directory to a variable
path = 'C:/Users/Dilshani/PycharmProjects/PythonFiles'

#assign the list of files in the specified directory(variable :path) to a list variable
dir_list = os.listdir(path)
#print the list
print(dir_list)

#creating a new text file
with open('C:/Users/Dilshani/PycharmProjects/PythonFiles/NewFile.txt' , 'w') as fp:
    pass

#check if the text file has been created
dir_list = os.listdir(path)
print(dir_list)

file = 'MyNewFile.txt'
dir_list = os.listdir(path)
print(dir_list)

# Creating a file at specified location
with open(os.path.join(path, file), 'w') as fp:
    pass
dir_list = os.listdir(path)
print(dir_list)

#open a file with read permission
with open("C:/Users/Dilshani/PycharmProjects/PythonFiles/List.txt", "r") as f:
    #read the whole document
    print(f.read())
    #read line by line
    #print(f.readlines())

#open a file with write permission
with open("C:/Users/Dilshani/PycharmProjects/PythonFiles/List.txt", "w") as f:
    #write in the text document
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    f.write('Python files handling')

#open a file with append permission
with open("C:/Users/Dilshani/PycharmProjects/PythonFiles/List.txt", "a") as f:
    #append a new line to the text file
    f.write('\nPython automation scripting')

#read the text file
with open("C:/Users/Dilshani/PycharmProjects/PythonFiles/List.txt") as f:
    print(f.read())

#close the file
f.close()
