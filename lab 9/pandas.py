import pandas as pd
import numpy as np
# Create two Series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

# Arithmetic operations
print("Addition:\n", s1 + s2)
print("\nSubtraction:\n", s1 - s2)
print("\nMultiplication:\n", s1 * s2)
print("\nDivision:\n", s1 / s2)
data = {'a': 100, 'b': 200, 'c': 300}
series = pd.Series(data)
print("Pandas Series from dictionary:\n", series)
# From a list
list_data = [10, 20, 30]
series_from_list = pd.Series(list_data)
print("Series from list:\n", series_from_list)

# From a NumPy array
array_data = np.array([1, 2, 3, 4])
series_from_array = pd.Series(array_data)
print("\nSeries from NumPy array:\n", series_from_array)

# From a dictionary
dict_data = {'x': 9, 'y': 8, 'z': 7}
series_from_dict = pd.Series(dict_data)
print("\nSeries from dictionary:\n", series_from_dict)
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

# Vertical stacking (simply concatenate)
vertical = pd.concat([s1, s2], ignore_index=True)
print("Vertical stacking:\n", vertical)

# Horizontal stacking (side by side as columns in a DataFrame)
horizontal = pd.concat([s1, s2], axis=1)
horizontal.columns = ['Series1', 'Series2']
print("\nHorizontal stacking:\n", horizontal)
