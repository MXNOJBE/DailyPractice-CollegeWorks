import pandas as pd
import numpy as np
import statistics as stats
df = pd.read_csv("Q8_MortalityDataset.csv")
# a1
print("number of variables are :\n", df.shape)
print("number of observations are \n:", len(df.axes[1]))
col_list = []
for col in df.columns:
    col_list.append(col)
print(col_list)

# A
print("\nAll rows and first 3 cols\n", df[:3])

# B
print("\nFirst 10 rows and all columns\n", df[10:])

# C
print("\n10 to 15 rows of first and 4th column\n", df[10:16][["AGE", "CHOL"]])

# D
print("Observation of 5th row 2nd column is:\n", df.iloc[3, 1])

# structure

print(df.info())

# extract
col23 = (df[['HEIGHT', 'WEIGHT']])
print("Col23 is:\n", col23)

# blood groups
print("Unique value in blood column are\n", len(df['BLOOD'].unique()))

# uniquesmokers

lssmoke = print((df['SMOKE'].unique()))

# cholest>300
ischol = len(df[df['CHOL'] > 300])
print("Chol greater than 300:", ischol)
