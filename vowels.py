
# 5.Write a Python program to test whether a passed letter is a vowel or not.

n=input("Enter a letter: ")
if n.lower() in 'aeiou':
    print(n,'is a vowel')
else:
    print(n,'is not a vowel')