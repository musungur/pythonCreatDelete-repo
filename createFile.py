# Creating a new file
import os
newfile = input("\ncreate new filename: ")
xtn = input("file extension: ")

try:
    with open(f"{newfile}.{xtn}","w") as nf:
        if newfile != "":
            if xtn == "py":
                crt = nf.write("'''new python file'''\n# python")
                print(f"filename '{newfile}.{xtn}' created.")
            elif xtn == "yml" or xtn == "yaml":
                crt = nf.write("---\n# new yaml file'''\n")
                print(f"filename '{newfile}.{xtn}' created.")
            elif xtn == "html":
                crt = nf.write("<!---new html file--->\n/*html*/")
                print(f"filename '{newfile}.{xtn}' created.")
            elif xtn == "ini":
                crt = nf.write("# new ini file'\n")
                print(f"filename '{newfile}.{xtn}' created.")
            elif xtn == "css":
                crt = nf.write("body\{\ncolor:\"red\";\n}'\n")
                print(f"filename '{newfile}.{xtn}' created.")
            elif xtn == "php":
                crt = nf.write("# new php file'''\n")
                print(f"filename '{newfile}.{xtn}' created.")
            elif xtn == "":
                crt = nf.write("#new php file'''\n")
                print(f"filename '{newfile}.{xtn}' created.")
            '''
            .
            and many file extension
            .
            .
            '''
        else:
            print("\nno file name given!")
except Exception as err:
    print(err)
