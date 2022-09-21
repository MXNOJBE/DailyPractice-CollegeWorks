import numpy as np
a = np.array([[2,1],[0,3]])
b = np.array([[5,4],[2,-1]])

print(f"The sum is {np.add(a,b)}")
print(f"The difference is {np.subtract(a,b)}")
print(f"The product is {np.multiply(a,3)}")
print(f"The product is {np.multiply(b,-2)}")

a1 = np.zeros([3,3])
print("Null matirx is: " ,a1)

a2 = np.identity(3)
print("Identity Matrix is : ",a2)
Name = ('name1', 'name2', 'name3', 'name4', 'name5')
Name1 = list(Name)
Score = (10, 20, 30, 40, 50)
Score1 = list(Score)
Attempts = (1, 3, 2, 1, 3)
Attempts1 = list(Attempts)
Qualify = ('yes', 'no', 'yes', 'no', 'yes')
Qulaify1 = list(Qualify)
        
a = np.array([('name1', 10,1,'yes'), ('name2', 20,3,'no'),('name3', 30,2,'yes'), ('name4', 40, 1,'no'),('name5',50,3,'yes')],
       dtype=[('Name', (np.str_, 10)), ('Score', np.int32), ('Attempts', np.int32),('Qulaify', (np.str_,10))])
fancy = [1,2,3]
print("Fancy indexing:",a[fancy])
#fancy
print("Structure is ",a.dtype)
#change the value of coloumn 2 and 3 
print("The un-altered:",a)
data = np.array(a[['Score','Attempts']])
print("The altered :",data)
#10 statistical summary
print(np.median(a['Score']))
print(np.sum(a['Score']))
print(np.max(a['Score']))
print(np.min(a['Score']))
print(np.argmax(a['Attempts']))
print(np.argmax(a['Attempts']))
print(np.argmax(a['Score']))
print(np.argmin(a['Score']))
print(np.median(a['Score']))
print(data)
