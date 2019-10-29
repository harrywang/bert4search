import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats
import statistics

# This project is for the evaluation step for summer paper.
# Before run this project, you should have the firms in S&P 500 Index and their top related firms from the pre-training steps.

# Import data from pre-training steps.
df = pd.read_csv("/Users/rachelzheng/Documents/GitHub/bert4search/data/top10firms_trainstep5000.csv")
# In "df", it contains the target firm in S&P 500 Index and the top 10 related firms from pre-training.

# Import the file contains Ticker, Company Name and GIC Sectors.
stock = pd.read_excel("sic_sp500.xlsx")
# In "stock", it contains the CIK number, Ticker, Company Name, GIC Sectors.

# Match the cik to sticker.
def to_ticker(df, left_name):
    df1 = pd.merge(df, stock[["CIK Number", "Ticker Symbol"]], how='left',left_on=left_name,right_on="CIK Number")
    df2 = df1["Ticker Symbol"]
    return df2

column_name = ["target", "top1", "top2", "top3", "top4", "top5", "top6", "top7", "top8", "top9", "top10"]

t = to_ticker(df=df["target"], left_name = "target")
for i in range(1,11,1):
    t1 = to_ticker(df=df[column_name[i]], left_name = column_name[i])
    t = pd.concat([t,t1],axis=1)

# "t" contains the ticker for candidate firms.
c = ["target_ticker", "top1_ticker", "top2_ticker", "top3_ticker", "top4_ticker", "top5_ticker", "top6_ticker",
             "top7_ticker", "top8_ticker", "top9_ticker", "top10_ticker"]
t.columns = c

# Similar to the previous match step, we also need to have the monthly return information for each cell in the company.
# Import the return file (2017)
r = pd.read_excel("return_div_2017.xlsx", sheet_name="WRDS")

time = ["02/28/2017", "03/31/2017", "04/28/2017", "05/31/2017", "06/30/2017","07/31/2017", "08/31/2017", "09/29/2017",
        "10/31/2017", "11/30/2017", "12/29/2017"]

def to_return(select):
    df1 = pd.merge(t[select], rt[["Ticker Symbol", "Returns"]], how='left', left_on=select, right_on="Ticker Symbol")
    df2 = df1["Returns"]
    return df2

r2 = []

for i in range(len(time)):
    rt = r[r["Names Date"] == time[i]]

    for i in range(len(c)):
        if i == 0:
            d = to_return(select = c[i])
        else:
            dt = to_return(select = c[i])
            d = pd.concat([d,dt],axis=1)

    # Run regression on each month data
    dt = d.fillna(0)

    dt["Ave"] = dt.iloc[:,1:11].mean(axis=1)

    model = LinearRegression()

    y = dt.iloc[:,0].values.tolist()
    x = dt["Ave"].values.tolist()

    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    print("R-squared: %f" % r_value ** 2)
    r2.append(r_value ** 2)

# Print the average final R^2
print("The average R^2 is: %f" % statistics.mean(r2))



