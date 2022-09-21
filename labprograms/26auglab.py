import re
import datetime

dob = input("Enter your Date of Birth: ")
for x in dob:
    if x == ' ':
        raise Exception("Your Date of birth cannot be empty")
    elif x == '?':
        raise Exception(
            "Please enter the date in the any format but using the slash('/')")
    elif x[0] == 'q' or x[0] == 'Q':
        print("Bye! Hope you run this program again")
        exit()
print(dob)
day1, month1, year1 = dob.split("/")
day1 = int(day1)
month1 = int(month1)
year1 = int(year1)
t_date = input("Enter todays date: ")
print(t_date)
#t_date = t_date.replace("/", '')
day2, month2, year2 = t_date.split("/")
day2 = int(day2)
month2 = int(month2)
year2 = int(year2)
dayfin = abs(day2-day1)
age = print(
    f"Your are {year2-year1}year {month2-month1}month's and {dayfin}days's old!")




def MyScottishAccent(word):
    accent = re.sub('o', 'u', word)
    print(accent)

MyScottishAccent("\nhello python coders")
MyScottishAccent("\ncompter nerd")
