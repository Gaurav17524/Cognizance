# Write a program to accept a string from the user and display characters, 
# that are present at an even index number.

s = input("enter the string: ")
l = len(s)
for i in range(0,l,2):
    print(s[i])
    


