# def sum(a=1, b=1, c=1):
#    print(a+b+c)


#a = sum(1, 2, 3)
# print(a)

# recursion
# def fact(k):
#    if(k<0):
#        result  = k* fact(k-1)
#        print(result)
#    else:
#        result = 1
# return result
#f = fact(3)
#print("Factorial of given number is =  ",f)
# passing lost as an arguement for function
'''
def f7(x):
    x.append(55)
    a = [10, 20, 30]
    f7(a)
    print(a)


def x(a, b): return a*b


print(x(a=10, b=10))


print(x(5, 6))


def f(x, y, z=0, w=0): return x+2*y+3*z+4*w


print(f(1, 2))
print(f(1, 2, 3))
print(f(1, 2, w=3))


def f(x, w, y=0, z=0): return x+2*y+3*z+4


print(f(1, 2, 3, 4))



def element():

    x = 0
    while x < 5:
        ele = int(input("enter the element")).split()
        a = []
        a.append(ele)
        x += 1
    print(a)


element()

# create a python program using function to find minimum and maximum in a list
# create a new list by multipying by maximum element with each element in the list
#  create a new list by and subtract by minimum element with each element in the list


def maxmin():
    elements = int(input("enter the elements"))
    list = elements.split()
    print("identifying the max and min")
    for num in elements:
        if(elements[0] > elements[1]):
            print("greater is ", elements[0])
        elif():
            print("greater is ", elements[1])


maxmin()



input_string = int(input("Enter a list element separated by space: "))
list = input_string.split()
print(list)
max = print("Maximum in the list is ", max(list))
min = print("Minimum in the list is", min(list))
print(max)
print(min)
max_list = [i * int(max) for i in list]
print(max_list)

elements = int(input("Enter the elements: "))
list = elements.split()
#list = [10, 20, 30, 50, 40]
list.sort()
print(list)
max = list[-1]
min = list[0]
print("max number is ", max)
print("min number is ", min)
max_list = [x * max for x in list]
print(max_list)
min_list = [x * min for x in list]
print(min_list)

input_string = int(input("Enter a list element separated by space:"))
list = input_string.split(",")
print(list)
'''

input_string = input("Enter a list element separated by space: ")
list = input_string.split(",")
print(list)
max = print("Maximum in the list is ", max(list))
min = print("Minimum in the list is", min(list))
print(max)
print(min)
#max_list = [i * int(max) for i in list]
# print(max_list)


#1-Aug-2022

