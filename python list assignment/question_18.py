# Take user input to create a list and display it.
user_input = input("Enter items separated by commas: ")
items = [item.strip() for item in user_input.split(",")]
print(items)
