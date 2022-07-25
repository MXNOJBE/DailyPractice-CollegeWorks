"""
Complete the following question and submit your PYTHON file with the output

1. What are the values of the following expressions?


(a) 1 + 3 ∗ 2 − 5 + 4


(b) 1 + 3 ∗ (2 − 5) + 4


(c) 5**2**2*3+1


(d) 5**(2**2)*3+1


(e) 1+3/2

2. Write a program that asks for user input and performs



(a) Celsius to Fahrenheit conversion.
(b) Pound
to kilogram conversion.
(c) asks the user for three integers a,
b and c, and prints out the largest among them. If there is more than one largest value (e.g. a=b
and a>c), print ‘Tie’.
"""



# question(a)
a = (1+3*2-5+4)
print("Answer for the expression (1+3*2-5+4) is {}".format(a))
# question(b)
b = (1+3*(2-5)+4)
print("Answer for the expression (1+3*(2-5)+4) is {}".format(b))
# question(c)
c = (5**2**2*3+1)
print("Answer for the expression (5**2**2*3+1) is {}".format(c))
# question(d)
d = (5**(2**2)*3+1)
print("Answer for the expression (5**(2**2)*3+1) is {}".format(d))
# question(e)
e = (1+3/2)
print("Answer for the expression (1+3/2) is {}".format(e))


#<=================================================>#
# Celsius to Fahrenheit conversion
#formula (F=C*1.8+32)
cel_temp = float(input("Enter the Temperature in Celcius:"))
far_temp = float(cel_temp*1.8+32)
print(("{}° celcius is equal to {} faranhiet").format(cel_temp, far_temp))


#<=================================================>#
# Pound to kilogram conversion
#formula (Kg=Pnd*0.45359237)
Pnd = float(input("Enter the Weight in pound:"))
Kg = (Pnd*0.45359237)
print(("{} pounds is equal to {} Kilograms").format(Pnd, Kg))

#<=================================================>#
a, b, c = int(input("Enter the value of a ")), int(
    input("Enter the value of b ")), int(input("Enter the value of c "))
if (a > b) and (a > c):
    print("a is greater")
elif (b > a) and (b > c):
    print("b is greater")
elif (c > a) and (c > b):
    # Prints out the largets value amongst the three values
    print("c is greater")
else:
    # Prints out "TIE" only if the largest value is same as the other variable
    print("Tie")
