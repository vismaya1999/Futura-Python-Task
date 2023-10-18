
# 6. Write a Python program that accepts a filename from the user and prints the extension of the file.

filename = input("Input the Filename: ")
f_extns = filename.split('.')
print ("Extension of filename is : " + "." + f_extns[-1])