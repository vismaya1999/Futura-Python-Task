
#  1. Input a list from user and extract Unique and duplicate values into a new list

l = list(map(int, input("Enter values to list ").split()))
duplicate = []
unique = []

for i in range(len(l)):
    if i < len(l)-1 and l[i] == l[i+1]:
        duplicate.append(l[i])
    elif l[i] not in duplicate:
        unique.append(l[i])
    else:
        pass

print("Duplicates:", duplicate)
print("Unique:", unique)











