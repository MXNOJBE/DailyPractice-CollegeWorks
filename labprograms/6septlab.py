import pandas as pd
import numpy as np
import statistics as stats
data = pd.read_csv("Q8_MortalityDataset.csv")
# print(data.describe())

# Q1a convert pd dataframe to structured array
stArray = np.zeros(len(data.values), dtype=[('age', 'i4'), ('height', 'i8'), ('weight', 'i8'), (
    'chol', 'i8'), ('smoke', 'U6'), ('blood', 'U2'), ('mort', 'U5')])
stArray['age'] = data['AGE']
stArray['height'] = data['HEIGHT']
stArray['weight'] = data['WEIGHT']
stArray['chol'] = data['CHOL']
stArray['smoke'] = data['SMOKE']
stArray['blood'] = data['BLOOD']
stArray['mort'] = data['MORT']
print("Strutured Array\n", stArray)

# Q2b
print("The number of variables are", stArray.size)
print("Index values are", stArray.dtype.names)

# Q3c
print("A. All rows and 3 cols\n", stArray[["age", "height", "weight"]])
print("B. 10 rows and all cols\n", stArray[0:10])
print("C. 10 to 15 rows and first, fourth cols",
      stArray[10:16][["age", "chol"]])
print("D. 5 row and second col", stArray[4][1])

# Q4d
print("Structure of array is", stArray.dtype)

# Q5e
col23 = np.array(stArray[['height', 'weight']])
print(col23)

# Q6f
for i in ['age', 'height', 'weight', 'chol']:
    var = stArray[i]
    print(f"\nStats on {i} column")
    print("Mean=", np.mean(var))
    print("Median=", np.median(var))
    print("Mode=", stats.mode(var))
    print("Standard Deviation=", np.std(var))
    print("Variance=", np.var(var))
    print("Minimum Value=", np.min(var))
    print("Maximum Value=", np.max(var))
    print("Range=", np.ptp(var))
    print("Coeff. of range=", round(
    np.ptp(var)/(np.max(var)+np.min(var)), 2))
    print("Sum=", np.sum(var))

# Q7g

print("Unique value in blood column are", len(np.unique(stArray[['blood']])))

# Q8h
lssmoke = [np.unique(stArray[['smoke']])[x][0]
           for x in range(0, len(np.unique(stArray['smoke'])))]
print("list of unique smoke columns are", lssmoke)

# Q9i
print("Cholestrol values above 300 are", len(stArray[stArray['chol'] > 300]))

# Q10j
print("Mean height of alive people is", round(np.mean(
    stArray[stArray['mort'] == "alive"]['height']), 2))

# Q11k
print("Age of tallest O blood group person is", stArray[stArray['height'] == np.max(
    stArray[stArray["blood"] == "o"]['height'])]["age"][0])

# Q12l
alive = stArray[stArray['mort'] == "alive"]
print("non smokers alive and below 40 years", len(
    alive[np.logical_and(alive['smoke'] == "nonsmo", alive["age"] < 40)]))
