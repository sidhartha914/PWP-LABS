def count_occurrences(tup, element):
    return tup.count(element)

my_tuple = (1, 2, 2, 3, 4, 2)
print("Occurrences of 2:", count_occurrences(my_tuple, 2))
def element_exists(tup, element):
    return element in tup

my_tuple = ('a', 'b', 'c')
print("Is 'b' in tuple?", element_exists(my_tuple, 'b'))
print("Is 'z' in tuple?", element_exists(my_tuple, 'z'))
def tuple_to_string(tup):
    return ''.join(map(str, tup))

my_tuple = ('H', 'e', 'l', 'l', 'o')
print("Tuple as string:", tuple_to_string(my_tuple))
def max_min(tup):
    return max(tup), min(tup)

my_tuple = (10, 5, 7, 20, 3)
maximum, minimum = max_min(my_tuple)
print("Maximum:", maximum)
print("Minimum:", minimum)
def tuple_strings_to_single_string(tup):
    return ' '.join(tup)

my_tuple = ('Python', 'is', 'fun')
print("Single string:", tuple_strings_to_single_string(my_tuple))
def sort_tuple(tup):
    return tuple(sorted(tup))

my_tuple = (3, 1, 4, 2, 5)
print("Sorted tuple:", sort_tuple(my_tuple))
def first_and_last(tup):
    if not tup:
        return None, None  # Handle empty tuple
    return tup[0], tup[-1]

my_tuple = (10, 20, 30, 40)
first, last = first_and_last(my_tuple)
print("First element:", first)
print("Last element:", last)
