def EncodeQR(s):
    pad=128
    pad=int(format(pad,"b"))
    pad_bin=""
    for i in range(0,len(s)):
        temp_int=ord(s[i])
        temp_bin=format(temp_int,"b")
        pad>>i
        pad_bin+=str(pad)+str(temp_bin)
    if(len(pad_bin)>70):
        print(pad_bin+"00")
    elif(len(pad_bin)>70):
        print(pad_bin+"00")
    else:
        print(pad_bin)
        
