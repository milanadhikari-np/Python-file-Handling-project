from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")


def createfile():
    try:
        readfileandfolder()
        name=input("Please tell your file name :-")
        p=Path(name)

        if not p.exists():
            with open(p,'w') as fs:
                data=input("Enter what  you want to write in this file:-")
                fs.write(data)
                print("File has been created sucessfully")
        else:
            print("This file already exits")
    except Exception as err:
        print(f"An error occured as {err}")



def readfile():
    try:
        readfileandfolder()
        name=input("Please tell which file you want to read:-")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("File has been read sucessfully")
        else:
            print("This file doesnot exists")

    except Exception as err:
        print(f"An error occured as {err}")


def updatefile():
    try:
        readfileandfolder()
        name=input("Please tell which file you want to update :- ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file :- ")     
            print("Press 2 for overwritting the data in your file :- ")     
            print("Press 3 for appending the content in your file :- ")

            res=int(input("Tell your Response :-"))

            if res==1:
                newname=input("Tell your new file name :- ")
                p2=Path(newname)  
                p.rename(p2)

            if res==2:
                with open(p,'w') as fs:
                    data=input("Enter your data you want to overwrite :- ")
                    fs.write(data)
            if res==3:
                with open(p,'a') as fs:
                    data=input("Enter your data you want to append :- ")
                    fs.write(""+data)


    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name=input("Please tell the file you want to delete :- ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File remove sucessfully")
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occured as {err}")


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check=int(input("Please tell your response:-"))

if check==1:
    createfile()

if check==2:
    readfile()

if check==3:
    updatefile()

if check==4:
    deletefile()
