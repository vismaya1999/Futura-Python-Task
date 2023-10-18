
# 2. Write a python program to check entered number is between 100-700 or 700-900

n= int(input("Enter value to check: "))
if n>100 and n<700:
    print(n,"is between 100-700")
elif n>700 and n<900:
    print(n,"is between 700-900")
else:
    print("Not in the range")