import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/HP/Data of credit card/creditcard_d.csv")

df.head()
print(df)

# Let's find how many columns are empty
missing_values_count = df.isnull().sum()

# We need to find missing values in the form of percentage
# we can find using the (total_missings/total_cells)*100

total_missings = missing_values_count.sum()

# let's find the total_cells
total_cells = np.product(df.shape)

# Let's find how much percentage of the value is missing
percent_missing = (total_missings/total_cells)*100

print(percent_missing)

# From above example, you can see that our data has no missing values










