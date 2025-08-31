def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

numbers = [2, 3, 4]
print("Product of all items:", multiply_list(numbers))
def largest_number(lst):
    return max(lst)

numbers = [10, 20, 5, 40, 25]
print("Largest number:", largest_number(numbers))
def remove_duplicates(lst):
    return list(set(lst))

items = [1, 2, 2, 3, 4, 4, 5]
print("List after removing duplicates:", remove_duplicates(items))
def remove_duplicates_ordered(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
from collections import Counter

def frequency(lst):
    return Counter(lst)

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print("Frequency of elements:", frequency(items))
def common_items(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Common items:", common_items(list1, list2))
def list_to_integer(lst):
    return int(''.join(map(str, lst)))

numbers = [1, 2, 3, 4]
print("Single integer:", list_to_integer(numbers))
