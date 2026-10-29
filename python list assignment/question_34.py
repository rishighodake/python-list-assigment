# Find common elements between two lists.
first_list = [1, 2, 3, 4]
second_list = [3, 4, 5, 6]
common = [item for item in first_list if item in second_list]
print(common)
