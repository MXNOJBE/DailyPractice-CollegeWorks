import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics
data=pd.read_csv("Q8_MortalityDataset.csv")
print(data)
#Q-1
data.shape
print("The Number of Variables are",data.shape[1])
print("The Number of Obesrvations are",data.shape[0])

#Q-2

print("All rows and 3 columns\n",data[["AGE","HEIGHT","CHOL"]])
print("Firtst 10 rows and all columns\n",data.iloc[0:10])
print("10 to 15 rows of first and 4th column\n",data[["AGE","CHOL"]].iloc[9:15])
print("Observation of 5th row 2nd column",data["HEIGHT"].iloc[4])

#Q-3
print(data)

#Q-4
df=pd.DataFrame(data[["HEIGHT","WEIGHT"]])
print(df)

#Q-6
print("Different Blood group",data["BLOOD"].unique())

#Q-7
print("Unique Smoke categories",data["SMOKE"].unique())

#Q-8
count=0
for i in range(len(data["CHOL"])):
               if data["CHOL"][i] > 300:
                   count=count+1
print("The number of people with chol level greater than 300 is",count)


#Q-9
print("Mean Hegiht of alive people is")
l=[]
for i in range(len(data["MORT"])):
    if data["MORT"][i]=="alive":
        
        l.append(data["HEIGHT"][i])

x=statistics.mean(l)
print(x)
l1=[]
for i in range(len(data["BLOOD"])):
    if data["BLOOD"][i]=="o":
        l1.append(data["HEIGHT"][i])

print("The maximum height with blood group o",max(l1))



#Q-10

for i in range(len(data["SMOKE"])):
    if data["SMOKE"][i]=="nonsmo":
        if data["MORT"][i]=="alive":
            if data["AGE"][i] <40:
                count=count+1

print("nonsmokers are alive who are below 40 years",count)



#2 graph Building
Avg=list(data.groupby("MORT")["AGE"].mean())
Type=list(data["MORT"].unique())
plt.pie(Avg,autopct='%1.1f%%')
plt.title("Pie chart")
plt.legend(Type)
plt.show()




plt.bar(Type,Avg,color=["yellow","blue","green"],width=0.4)
plt.title("Bar plot")
plt.xlabel("Mortality")
plt.ylabel("Age")
plt.show()



data.groupby("MORT")["AGE"].plot.line()
plt.show()


data["AGE"].plot.box(color="g")
plt.title("Box plot")
plt.ylabel("Age Values")
plt.show()



        





