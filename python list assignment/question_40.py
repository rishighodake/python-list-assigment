# Demonstrate the list methods.
items = [3, 1, 2, 2]

items.append(4)
print("append:", items)

items.extend([5, 6])
print("extend:", items)

items.insert(0, 0)
print("insert:", items)

items.remove(2)
print("remove:", items)

removed_item = items.pop()
print("pop:", items, "| removed:", removed_item)

print("index of 3:", items.index(3))
print("count of 2:", items.count(2))
print("copy:", items.copy())

items.sort()
print("sort:", items)

items.reverse()
print("reverse:", items)

items.clear()
print("clear:", items)
