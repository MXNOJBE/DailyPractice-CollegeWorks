from operator import index
import mod


def EncodeQR(s):

    for letter in s:
        binary = mod.conv(s)
        if(index(letter) == 0):
            binary = binary.rjust(50, "10000000")
        elif(index(letter == 1)):
            binary = binary.rjust(50, "01000000")

    if len(binary) > 50:
        final = binary.append("000")
    elif len(binary) > 70:
        final = binary.append("00")

    print("The Final Encoded String : ", final)


while 1:
    s = input("Enter a String: ")

    if(len(s) > 7):
        print("The String is too large")
    elif(len(s) < 1):
        print("The String is too Short")

    else:
        break

EncodeQR(s)
