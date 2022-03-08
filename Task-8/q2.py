#program to check whether two array are equal
import numpy as np
a = int(input("enter the length of first array"))
b = int(input("Enter the length of second array"))
ar_a = []
ar_b = []
if a == b :
    print("Enter the element of first array")
    for i in range(a):
        ar_a.append(input())
    print("Enter the element of second array")
    for i in range(b):
        ar_b.append(input())
    leng = len(ar_a)
    ar_aa = np.sort(ar_a)
    ar_bb = np.sort(ar_b)  
    print(ar_aa,type(ar_aa))
    print(ar_bb,type(ar_bb))
    print(np.array_equal(ar_aa, ar_bb))
    




    
    
