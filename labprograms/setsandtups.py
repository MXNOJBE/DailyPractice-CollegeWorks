#1)
print("Program 1 Starts here")
tup = [ ('main st.', 4, 4000), ('elm st.', 1, 1200), ('pine st.', 2, 1600)]
tup.sort(key= lambda x: x[1])
print("Sorted in ascending order by number of rooms ",tup)

tup.sort(key= lambda x:x[2])
print("Sorted in ascending order of price ",tup)

tup.sort(key= lambda x: x[2]/x[1] )
print("Sorted in ascending order of price-per-room ",tup)
print("Program 1 Ends here\n")

#2)  
print("Program 2 Starts here")
i = 0
while i<2:
    def pay(wage,hrs):
      if(hrs>40):
        return 1.5*(hrs-40)*wage+(wage*40)
      else:
        return (wage*hrs)

    hourlywage=float(input("Enter hourly wage of employee : "))
    workinghours=int(input("Enter number of hours the employee worked : "))

    print("The employee's pay is : Rs ",pay(hourlywage,workinghours))
    i+=1
print("Program 2 Ends here\n")

#3)
print("Program 3 Starts here")
stock = []
ch = 1
while(1):
    stock_temp = []
    buy_stock = sell_stock = 0.0
    if(ch == 1):
        name = input("Enter Company Details : ")
        quant = int(input("Enter quantity of stocks : "))
        price = float(input("Enter price : "))
        status = input(
            "Enter B for buying and S for selling (Please use Upper-Case): ")
        stock_temp.append(name)
        stock_temp.append(quant)
        stock_temp.append(price)
        if(status == "B" or status == "S"):
            stock_temp.append(status)
        else:
            print("****Invalid Input*****")
            break
        stock.append(tuple(stock_temp))
        ch = int(
            input("Do you wish to Add another Call? (Choose with Yes as 1 and 0 as No:)"))
        # stock=tuple(stock)
        continue
    elif(ch == 0):
        for i in stock:
            for status in i[3]:
                if(status == "B"):
                    buy_stock += float(i[1])*float(i[2])
                elif(status == "S"):
                    sell_stock += float(i[1])*float(i[2])
                else:
                    print("\nInvalid status")

        print("\nBuy : ", buy_stock, "\nSell : ", sell_stock)
        break
    else:
        print("I am going to call it tonight")
        break

print("Program 3 Ends here\n")
    
#4)
print("Program 4 Starts here")
len_a=int(input("Enter number of elements for set A : "))
len_b=int(input("Enter number of elements for set B : "))
a=set()
b=set()
for i in range(0,len_a):
        n=int(input(" Enter element for set A  : "))
        a.add(n)

for i in range(0,len_b):
          n=int(input(" Enter element for set B  : "))
          b.add(n)

#unique Elements in both sets
print("Set A : ",a)
print("Set B : ",b)

# Elements in A and B but not in both
set1=a.difference(b)
set2=b.difference(a)
q2=set1.union(set2)
print("Elements present in Set A and B but not in both : ",q2)

# Elements in both A and B
set3=a.intersection(b)
print("Elements present in both Set A and B are : ",set3)

#Update set B by adding items from Set A except common items
b.update(a)
b.difference(set3)
print("Updated Set B is  : ",b)
print("Program 4 Ends here")