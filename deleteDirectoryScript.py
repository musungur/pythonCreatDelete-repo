'''
Script to delete directory
'''
import os
import time

path = os.getcwd()
#print(f"{path}")

dire = input("Enter repo name to delete: ")
try:
    if dire != "":
        #chdir(path)
        os.rmdir(dire)
        print(f"'{dire}' deleted")
    else:
        print("You didnt specify repo name")
except Exception as err:
    print(err)
