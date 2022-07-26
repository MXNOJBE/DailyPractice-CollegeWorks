list_items = ["apple", "bannana", "grapes", "orange", "guava"]
print(list_items)
# print(list_items[:3])
list_items.append("mango")
print(list_items)
listed_items = list_items.copy()
print(listed_items)
counted = listed_items.count("apple")
print(counted)
list_items.insert(99, "1")
print(list_items)
listed_items.extend(list_items)
print(listed_items)
ind = list_items.index("1")
print(ind)
listed_numbers = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(listed_numbers)
listed_numbers.sort()
print(listed_numbers)
listed_numbers.sort(reverse=True)
print(listed_numbers)
popping = listed_items.pop(0)
print(popping)
# change list items
listed_items[1] = "Mercedes"
print(listed_items)
# replacing values in a list wiht one or more values
listed_items[0:4] = ["Mercedes", "Mclaren"]
print(listed_items)
