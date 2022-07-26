from cmath import sqrt
import math as m


meter_data = float(input("Enter the values in meter"))
foot_data = meter_data*3.28084
print(("Foot data is {}").format(foot_data))


# KM INTO MILES

km_data = float(input("Enter the values in kilometer"))
mile_data = km_data*0.62137119
print(("kilometer data is {}").format(mile_data))

# Area

side1 = 3
side2 = 4
side3 = 6
s = (side1+side2+side3)/2
area = m.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(s)
print(area)

# Integer

user_data = int(input("enter an integer to count number of digits"))
print(user_data)
n = user_data
count = 0
while(n > 0):
    count = count+1
    n = n // 10
print(count)

# interest

# (A/P)SQRT1/t-1
a = 3335.8
t = 3
p = 3000
interest = (a/p)**(1/3)-1
print(interest*100)

# 6
value = int(input("Enter the range"))
for i in range(1, value+1):
    print(f'{int(m.pow((-1),(i+1)))}/{2*i+1}', end=", ")

# 9


def calculate(power):
    if (power <= 200):
        charge = (0.5*power)
        print(charge)
    elif power in range(201, 400):
        charge = (100+0.65*power)
        print(charge)
    elif power in range(401, 600):
        charge = (230+0.5*power)
        print(charge)
    elif power in range(601):
        charge = (390+0.5*power)
        print(charge)


customers = ["aarav", "raghav", "madhav", "pranav"]
customer_name = (input("Enter customer name"))
if customer_name in customers:
    power = float(input("Enter the amount of units"))
    calculate(power)
    # print(calculate.charge)
    #print(customer_name + "welcome")
else:
    print("customer not present")
