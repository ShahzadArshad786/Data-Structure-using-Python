import numpy as np 
n = int(input("Enter Size of the Array : "))

arr = np.ndarray(shape = (n , ) , dtype = int)

for i in range(0 , n):
    arr[i] = int(input("Enter Array Element at index arr[%d] : " %i))

for i in range(0 , n):
    print(arr[i] , end = " ")

choice = int(input("Enter Your Choice : "))
match choice:

    case 1:
        print("haye")
    case _:
        print("Invalid choice")
