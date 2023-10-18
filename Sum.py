
#3. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

a,b,c=map(int,input('Enter 3 nos: ').split())
sum=a+b+c
if a==b==c:
    print(sum *3)
else:
    print(sum)