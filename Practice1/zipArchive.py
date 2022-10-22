import os
import zipfile as zf


archive = 'archive.zip'
file = input("What file do you want to add to this archive? ")
if file in os.listdir("allFiles"):
    file_place = 'allFiles/' + file
    with zf.ZipFile(archive, 'a') as zip:
        zip.write(file_place)
else:
    print(f"File {file} not found")


with zf.ZipFile(archive, mode='a') as zip:
    for item in zip.namelist():
        print(item)


answer = input("Do you want to delete the file? [y/n]: ")
if answer == 'y':
    if os.path.isfile(archive):
        os.remove(archive)
    else:
        print(f"Error: {archive} not found")