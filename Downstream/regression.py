# This program is used to calculate the R^2 for the regression part.

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy import stats

# Import the data for regression
df = pd.read_excel("/Users/rachelzheng/Desktop/bert4search_returnnodiv.xlsx",sheet_name="Dec")
#df = pd.read_excel("/Users/rachelzheng/Documents/GitHub/bert4search/downstream/sampling_returnnodiv.xlsx",sheet_name="Dec")

df = df.fillna(0)

df["Ave"] = df[["Company1","Company2"]].mean(axis=1)

model = LinearRegression()

y = df["Target"].values.tolist()
x = df["Ave"].values.tolist()

#model.fit(x,y)
#print("R-squared: %f" % model.score(x, y))

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print("R-squared: %f" % r_value ** 2)



