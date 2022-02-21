#Write a program to check if the given number is a palindrome number.

a =input("Enter any number")
b = len(a)
d=0
e = int(a)
f = int(a)
for i in range(b):
    c = e % 10
    d = d*10+c
    e = e // 10
if(d == f):
    print("True")

else:
    print("False")


