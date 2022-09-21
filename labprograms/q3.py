stock1 = []
stock2 = []
buy_stock=sell_stock=0
name = input("Enter the comp name")
stock2.append(name)
price = float(input("Price"))
stock2.append(price)
quant = int(input("Quant"))
stock2.append(quant)
action = input("Enter action")
if(action == 'B' or action == 'S'):
    stock2.append(action)
else:
    print("Invalid")
stock1.append(tuple(stock2))

for i in stock2:
    for action in i[3]:
        if(action=="B"):
            buy_stock +=float(i[1])*float(i[2])
        elif(action =="S"):
            sell_stock = (float(i[1])*float(i[2]))


