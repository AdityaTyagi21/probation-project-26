import numpy as np
import random

arr = np.random.randint(1,20, (3,3)) #generate a 3X3 array

#print the entire array
print("Original Array: ")
print(arr)

#print the first row of the array
print("\nFirst row: ")
print(arr[0])

#print the second column of the array
print("\nSecond column: ")
print(arr[: , 1])

#print the element at position (2,2)
print("\nElement at position (2,2): ")
print(arr[1,1])

#print the first two rows and first two columns
print("\nSub-array")
print(arr[:2 , :2])

#replace the middle element with 99
arr[1,1] = 99
print("\nArray after replacing middle element: ")

