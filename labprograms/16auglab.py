
"""
cricketer = {
    "Virat Kohli": "5 November 1988",
    "Umesh Yadav": "25 October 1987",
    "Manish Pandey": "10 September 1989",
    "Rohit Sharma": "30 April  1987",
    "Ravindra Jadeja": "6 December 1988",
    "Hardik Pandya": "11 October 1993",
}


def birthDate(t_name):
    i = 1
    for name, birthday in cricketer.items():
        if name == t_name:
            print(birthday)
            return
            i = 1
        else:
            i = 0
    if(i == 0):
        print("Not Found")


ch = 1


while(ch):
    name = input("Enter Full name of the Cricket Player : ")
    birthday = input("Enter birthday  : ")
    temp = {name: birthday}
    cricketer.update(temp)
    ch = int(input("Enter 1 to continue or 0 to discontinue :"))

print("Search Mode")
search_name = input("\nEnter name of cricket player you want birthday :")
birthDate(search_name)


s = "Wisdom is easily acquired when hiding ,under the bed with a saucepan on your head.He picked up trash in his spare time to dump in his neighbor's yard.I've never seen a more beautiful brandy glass filled with wine."
sent = s.split(".")
print(len(sent))
nums = [x for x in range(1, (len(sent)+1))]
print(nums)
dict1 = {nums[i]: sent[i] for i in range(len(sent))}
print(dict1)

"""
import encodeqr


sentence = input("Enter a string : ")
encodeqr.EncodeQR(sentence)
