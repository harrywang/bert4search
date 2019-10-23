import pandas as pd
import numpy as np
import random

# df contains the company information, SIC code and GICS sector code.
df = pd.read_excel("/Users/rachelzheng/Desktop/cla.xlsx")

data = pd.read_excel("/Users/rachelzheng/Desktop/top10firms.xlsx",sheet_name="top10firms")

w = data["ticker_target"].tolist()
#w.drop("MON")

# f corresponds to the final data for random sampling
f_gics = []
f_sic = []

for i in range(len(w)):
    t = df.loc[df["Ticker"] == w[i]]
    # Return the gics for the target company
    gics = t.iloc[0,3]
    # Return the SIC for the target company
    #sic = t.iloc[0,4]
    # Gather all companies in the same GICS division
    a = df.loc[df["GIC Sectors"] == gics]
    # Return the ticker of companies in the same GICS division
    a_list = a["Ticker"].tolist()
    a_list.remove(w[i])
    # Randomly select 10 firms from the list
    b = random.sample(set(a_list), 10)
    # Store everything in the f
    b.append(w[i])
    f_gics.append(b)

f = pd.DataFrame(f_gics)

f.columns = ["Company1","Company2","Company3","Company4","Company5",
             "Company6","Company7","Company8","Company9","Company10",
             "Target"]

f.to_excel("sampling.xlsx",index=None)

