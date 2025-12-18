from pathlib import Path
import os

# show all files and folders
def readfileandfolder():
    items = list(Path('.').glob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

# create file
def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occurred: {err}")

# read file
def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                print(fs.read())
            print("Read successfully")
        else:
            print("File doesn't exist")

    except Exception as err:
        print(f"An error occurred: {err}")

# update file
def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for renaming the file")
            print("Press 2 for overwriting the file")
            print("Press 3 for appending data")

            res = int(input("Tell your response: "))

            if res == 1:
                new_name = input("Tell new file name: ")
                p.rename(Path(new_name))
                print("File renamed successfully")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter new data: ")
                    fs.write(data)
                print("File overwritten successfully")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Enter data to append: ")
                    fs.write(" " + data)
                print("Data appended successfully")

            else:
                print("Invalid choice")

        else:
            print("File doesn't exist")

    except Exception as err:
        print(f"An error occurred: {err}")

# delete file
def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully")
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occurred: {err}")

# menu
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please tell your response: "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid option")
