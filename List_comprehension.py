from audioop import reverse


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
listed_items = ["Mercedes", "Mclaren",
                "Alipne", "RB", "Haas", "Williams", "AMR"]
print(listed_items)
cleaar = listed_items.clear()
# print(cleaar)


# 27/07/2022
#[print(x) for x in listed_items]

newlist = ['apple' for x in listed_items]
print(newlist)


newlist = [x if x != "abcd" else "orange" for x in list_items]
print(newlist)

newlist3 = [x for x in range(10)]
print(newlist3)

newlist4 = [x for x in range(10) if x <= 7]
print(newlist4)

# palindrome


def palindrome(n):
    l = list(str(n))
    r = l[:]
    r.reverse()
    if(l == r):
        return print("palindrome")
    else:
        print("not  a palindrome")


palindrome("apple")


# secondmethod


def palindrome(n):
    l = list(str(n))
    r = 1[::-1]  # directly reversing it
    # r.reverse()
    if(l == r):
        return print("palindrome")
    else:
        print("not a palindrome")
