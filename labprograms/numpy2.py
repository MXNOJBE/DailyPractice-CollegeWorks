import numpy as np
import pandas as pd
data = pd.read_csv("class_example.csv")
heights = np.array(data['height(cm)'])
print(heights)
print(data.head(5))
print(data.tail(5))
print(heights)
np.sum((heights>180) & (heights<189))
np.sum(~(heights<=180)|(heights>=189))
short = (heights < 175)
normal = (heights> 176) & (heights<185)
tall = (heights>185)

#find summary of three category of presidents

print("Stats of short presidents: ")
print("Median Height", np.median(heights[short]))
print("Maximum Height of SHORT presidents: ",np.max(heights[short]))
print("Average Height of SHORT presidents: ",np.mean(heights[short]))


#handling missing data

#none - object
vals1 = np.array([1,None,3,4])
vals1
#not possible to perform aggregations like sum() or min()
vals1.sum()
#NaN(acronym for not a number): Missing numerical data

#Nan is a bit like a data virus-it infects any other object it touches

#1+np.nan
vals2 = np.array([1,np.nan,3,4])
vals2.dtype
vals2.sum(),vals2.nammin(vals2),np.nanmax(vals2)
#methods doe detecting,removing, and replaccing null values in Pandas data structures
pdvals2 = pd.series(vals2)
padvals2.isnull()
