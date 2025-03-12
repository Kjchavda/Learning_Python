import os

file_path = "Py_Basics\\test.txt"

if os.path.exists(file_path):
    print("Exists")
else: 
    print("Doesnt exist")

with open(file_path, "r") as file:
    # file_contents = file.read()   # Reads and stores the whole contents in the variable
    # print(file_contents)
    #file_lines = file.readlines()   #Stores all the lines as different elements of the list
    #print(file_lines)               #file.readline would read the lines one at a time

    for line in file:
        print(line, end="")
    print()
    print() # blank lines

#Another controlled way to read a file is:

with open(file_path, 'r') as file:
    size_to_read = 50
    file_contents = file.read(size_to_read)

    while len(file_contents)>0:
        print(file_contents)
        file_contents = file.read(size_to_read)
#file.tell() #returns the position in the file where we are currently at
#f.seek(number) #used to go to a certain character