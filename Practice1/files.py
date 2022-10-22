import os

file = 'allFiles/text.txt'
with open(file, 'a') as file_handler:
    txt = input("Enter some text: ")
    file_handler.write(txt + '\n')


with open(file, 'r') as file_handler:
    data = file_handler.read()
    print("Data of the file:\n", data)


answer = input("Do you want to delete the file? [y/n]: ")
if answer == 'y':
    if os.path.isfile(file):
        os.remove(file)
    else:
        print(f"Error: {file} file not found" )