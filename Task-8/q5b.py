import numpy as np
arra = []
a = int(input("Size of first array:"))
for i in range(0,a):
    ele = int(input("Enter the elements of first array"))
    arra.append(ele)
arra = np.array(arra)
print("data type of an array :", arra.dtype)
arra = arra = arra.astype('float64')
print(arra)
print(arra.dtype)
