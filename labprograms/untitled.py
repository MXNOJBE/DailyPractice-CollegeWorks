
import re
import datetime

isvaliddate = True
try:

    birthdate = input("Enter your date of birth: ")
    day, month, year = birthdate.split("/")
    datetime.datetime(int(year), int(month), int(day))
    if(isvaliddate == True):
        print("Input date is valid")
        age = (2022-int(year))
        print("the age is", age)


except ValueError:
    isvaliddate = False
    if birthdate[0] == "":
        print("Enter the input")
        birthdate = input("Enter your date of birth")
    elif birthdate[0] == "?":
        print("Please enter data in dd\mm\yy format")
        birthdate = input("Enter your date of birth")
    elif birthdate[0] == "q" or birthdate[0] == "Q":
        print("Bye!")
        exit()
    if(isvaliddate):
        print("Input date is valid")

    else:
        print("input date is not valid")


def MyScottishAccent(string):
    print("Entered string is -\n", string)
    result = re.sub("o", "u", string)
    print("\nOutput String - \n", result)


MyScottishAccent("hello python coders")
MyScottishAccent("computer nerd")


def LonelyOne(num):
    print("\nEntered number is = ", num)
    count = 0
    a = re.search("11", num)
    if a:
        print(0)
    else:
        for i in range(len(num)):
            if num[i] == "1":
                count += 1
        print(f"1 is repeated {count} times.\n") if count != 0 else print("0")


LonelyOne("101")
LonelyOne("1111")
LonelyOne("444")
