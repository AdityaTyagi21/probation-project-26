import numpy as np
import random

arr1 = np.random.randint(1,21,10)
arr2 = np.random.randint(1,21,10)

print("Array 1: ", arr1)
print("Array 2: ", arr2)

#Element-wise addition
print("\nElement-wise Addition: ", arr1 + arr2)

#Element-wise subtraction
print("\nElement-wise Subtraction: ", arr1 - arr2)

#Element-wise multiplication
print("\nElement-wise Multiplication: ", arr1 * arr2)

#Element-wise division
print("\nElement-wise Division: ", arr1 / arr2)

# square every element in the first array
print("\nSquare of Array 1: ", arr1 ** 2)

#Dot product of the two arrays
print("\nDot Product: ", np.dot(arr1, arr2))

#Sort the second array in ascending order\
print("\nSorted Array 2: ", np.sort(arr2))