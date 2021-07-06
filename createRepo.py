'''
Create a folder
'''
import os
import time
path = os.getcwd()
print(f"{path}")

os.chdir(path)

Newfolder = input("create folder name: ")
try:
    if Newfolder != "":
        os.mkdir(Newfolder)
        print(f"\nYou've created a new folder '{Newfolder}'.")
    else:
        print("\nyou must enter the folder name in order to create")
except Exception as err:
    print(err)
