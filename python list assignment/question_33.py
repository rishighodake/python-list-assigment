# Find the second-largest distinct number in a list.
numbers = [12, 5, 19, 12, 8, 19]
unique_numbers = sorted(set(numbers))
if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("The list needs at least two distinct numbers.")
