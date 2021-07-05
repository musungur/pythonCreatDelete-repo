# deleting file
import time
import os
path = os.getcwd()

file = input("enter file name to delete: ")
try:
    if file != "":
        os.remove(file)
        print(f"'{file}' deleted")
    else:
        print("no file name entered")
except Exception as err:
    print(err)
