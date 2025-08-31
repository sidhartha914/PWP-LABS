import numpy as np
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix:\n", matrix)
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
common_values = np.intersect1d(arr1, arr2)
print("Common values:", common_values)
arr = np.array([1, 2, 3])
repeated = np.repeat(arr, 3)
print("Repeated elements:", repeated)
arr = np.array([1, 2, 3, 4, 5])
memory_size = arr.nbytes
print("Memory size of the array (in bytes):", memory_size)
ones_array = np.ones((3, 3))
zeros_array = np.zeros((2, 4))

print("Array of ones:\n", ones_array)
print("Array of zeros:\n", zeros_array)
arr = np.array([10, 20, 30, 40, 50])
fourth_element = arr[3]  # Indexing starts at 0
print("4th element:", fourth_element)
