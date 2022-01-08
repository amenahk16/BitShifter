import os
import re
path = input("Enter path of file ")
file = open(path, "+r")


charx=re.findall(r'.',"".join(file.readlines()))
choice = int(input("Enter shift number : "))

if (choice<0):
        print("preform left shift ")
        afterShift = [chr(ord(x) << (choice*-1)) for x in charx]
        file.seek(0)
        file.write("".join(afterShift))
        print("".join(afterShift))
elif (choice>0):
        print("preform right shift ")
        afterShift = [chr(ord(x) >> choice ) for x in charx]
        file.seek(0)
        file.write("".join(afterShift))
        print("".join(afterShift))
else:
        print("".join(charx))
