# SUM OF NUMBER FROM 0-N

def sumof(n):
    sum = 0
    for i in range(0,n+1):
        sum=sum+i
    print(sum)
n=int(input('Enter number to check Sum: '))
sumof(n)

# OR

value=input('Enter values: ')
l=value.split()
sum=0
for i in range(len(l)):
    sum=sum+i
print(sum)


