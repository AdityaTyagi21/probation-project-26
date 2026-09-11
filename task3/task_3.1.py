import numpy as np
import random

arr = np.random.randint(1, 101, size=10)  # Generate an array of 10 random integers between 1 and 100

print("Original Array: ", arr)

# maximum value in the array
max_value = np.max(arr)
print("Maximum Value: ", max_value)

# minimum value in the array
min_value = np.min(arr)
print("Minimum Value: ", min_value)

#mean value of the array
mean_value = np.mean(arr)
print("Mean value: ", mean_value)

#Sum of all elements in the array
sum_value = np.sum(arr)
print("Sum of all elements: ", sum_value)

#Index of the maximum value in the array
max_index = np.argmax(arr)
print("Index of Maximum Value: ", max_index)

#Index of the minimum value in the array
min_index = np.argmin(arr)
print("Index of Minimum Value: ", min_index)

#Sort the array in ascending order
sorted_arr = np.sort(arr)
print("Sorted Array: ", sorted_arr)


