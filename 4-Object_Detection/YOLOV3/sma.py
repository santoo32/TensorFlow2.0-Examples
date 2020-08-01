import pandas as pd
import numpy as np


product = {
    'time' : [1,2,3,4,5,6,7,8,9,10,11,12],
    'confidence':[290,260,288,0,0,0,0,0,0,0,0,0]
}

# Turns object into a data table
df = pd.DataFrame(product)
# Prints the table 
print(df)
# Prints the first n lines of the table
# print(df.head(n))


# SMA of 3
for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)

print(df)