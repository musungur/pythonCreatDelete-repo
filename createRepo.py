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
        print(f"\nYou've created a new folder with a '{Newfolder}'.")
    else:
        print("\nYou didnt specify name.")
except Exception as err:
    print(err)
