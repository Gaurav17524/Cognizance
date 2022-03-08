#addition of two numpy array
import numpy as np
arra = []
arrb = []
a = int(input("Size of first array:"))
b = int(input("Size of second array:"))
if a==b:
    for i in range(0,a):
        ele = int(input("Enter the elements of first array"))
        arra.append(ele)
    for i in range(0,b):
        ele = int(input("Enter the elements of second array"))
        arrb.append(ele)
    arra = np.array(arra)
    arrb = np.array(arrb)
    add_arr = np.add(arra,arrb)
    print("Added aray",add_arr)
else:
    print("Addition not possible of unequal arrays")


