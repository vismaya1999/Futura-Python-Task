
# 4. Write a Python program to count the number 4 in a given list[1,2,3,4,5,6,4,7,3,4] = three times 4 is occuring

l = list(map(int, input("Enter values to list ").split()))
count=0
n=int(input("No to check occurence: "))
for i in range(len(l)):
    if i<len(l) and n==l[i]:
        count=count+1

print(n,"occurs",count)