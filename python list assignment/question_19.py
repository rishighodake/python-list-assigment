# Remove duplicates from a list of 10 numbers, preserving order.
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)
