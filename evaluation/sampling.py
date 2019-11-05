# This project is for randomly sampling 10 firms from the same GICS6 and calculate the R^2 for monthly return.

import numpy as np
import pandas as pd
import random
from sklearn.linear_model import LinearRegression
from scipy import stats
import statistics

# Import the data contains GICS6 information
g = pd.read_excel("/Users/rachelzheng/Documents/GitHub/bert4search/data/sp500_GICS.xlsx",sheet_name="data")

# Group the data by GICS6
data = g.groupby(["GICS6"])

# Target firms
w = ['APD', 'SWKS', 'HES', 'AEP', 'AXP', 'AFL', 'AIG', 'UNM', 'AAL', 'ADI', 'APA', 'AMAT', 'ADM', 'ADP', 'AVY', 'BLL', 'BAX', 'BDX', 'HRB', 'BA', 'BMY', 'BF.B', 'CPB', 'STZ', 'CAT', 'CTL', 'JPM', 'CINF', 'CLX', 'KO', 'CL', 'CAG', 'TAP', 'GLW', 'CMI', 'TGT', 'DAL', 'CMA', 'DG', 'DOV', 'OMC', 'FLS', 'ECL', 'PKI', 'EMR', 'EFX', 'XOM', 'FITB', 'USB', 'MTB', 'FMC', 'F', 'BEN', 'GPS', 'GD', 'GE', 'GIS', 'GPC', 'HAL', 'HAS', 'HP', 'HSY', 'HPQ', 'HRL', 'HUM', 'HBAN', 'ITW', 'INTC', 'IBM', 'IFF', 'IP', 'IPG', 'JEC', 'KSU', 'K', 'KMB', 'KR', 'LEG', 'LLY', 'LNC', 'L', 'LOW', 'MMC', 'MAS', 'MKC', 'MCD', 'SPGI', 'CVS', 'ETR', 'MMM', 'MSI', 'BAC', 'NBL', 'JWN', 'ES', 'XEL', 'WFC', 'NTRS', 'NUE', 'PCAR', 'PH', 'PNR', 'PEP', 'PFE', 'PVH', 'PPG', 'PG', 'PGR', 'TRV', 'SLB', 'SHW', 'SJM', 'SNA', 'KEY', 'SO', 'BBT', 'LUV', 'CVX', 'SWK', 'STT', 'SYY', 'JEF', 'TXN', 'TMO', 'TIF', 'TSN', 'UAL', 'UNP', 'MRO', 'UTX', 'VFC', 'WMT', 'WDC', 'WY', 'WHR', 'WMB', 'TJX', 'ZION', 'JNJ', 'VAR', 'TXT', 'GWW', 'CSX', 'MRK', 'SYK', 'DHR', 'CHD', 'DE', 'RHI', 'AON', 'SCHW', 'AMGN', 'KLAC', 'NKE', 'AAPL', 'UHS', 'FLIR', 'HD', 'LB', 'NSC', 'LRCX', 'EA', 'PNC', 'D', 'ATVI', 'CAH', 'MU', 'CTAS', 'PAYX', 'O', 'JBHT', 'UNH', 'VZ', 'T', 'VTR', 'XLNX', 'ROST', 'EXPD', 'STI', 'NEE', 'MO', 'BBY', 'PNW', 'HCP', 'WELL', 'ADSK', 'HON', 'WEC', 'PEG', 'MSFT', 'HOG', 'M', 'ADBE', 'OXY', 'FISV', 'QCOM', 'CERN', 'CMS', 'CBS', 'NWL', 'CCL', 'FAST', 'CELG', 'XRAY', 'AMP', 'APH', 'EOG', 'PHM', 'WM', 'EIX', 'MCHP', 'SBUX', 'C', 'FCX', 'JCI', 'SYMC', 'MHK', 'COG', 'CSCO', 'HCA', 'MNST', 'AZO', 'REGN', 'AES', 'HIG', 'BIIB', 'VRTX', 'CTXS', 'KIM', 'GILD', 'DHI', 'ROP', 'RCL', 'KSS', 'BSX', 'GS', 'MS', 'CB', 'INTU', 'ORLY', 'ALL', 'VNO', 'ALXN', 'EQR', 'BWA', 'COST', 'MAC', 'IVZ', 'EMN', 'AVB', 'MLM', 'TSCO', 'LH', 'ESS', 'LEN', 'PPL', 'AIV', 'DVA', 'COF', 'MCK', 'DLTR', 'DTE', 'LMT', 'DRI', 'HSIC', 'WAT', 'EL', 'NTAP', 'AEE', 'AMG', 'SEE', 'NRG', 'VRSN', 'ETFC', 'AMZN', 'IRM', 'NOV', 'DGX', 'ROK', 'FE', 'SRE', 'VLO', 'ISRG', 'RL', 'BXP', 'AME', 'PXD', 'OKE', 'SLG', 'YUM', 'CHRW', 'JNPR', 'PLD', 'NVDA', 'RTN', 'ED', 'MAR', 'FFIV', 'FDX', 'PWR', 'CCI', 'AMT', 'CMG', 'CTSH', 'MCO', 'RSG', 'SPG', 'EBAY', 'NFLX', 'URI', 'BRK.B', 'HST', 'BKNG', 'AKAM', 'DVN', 'UPS', 'A', 'MET', 'EW', 'ADS', 'EQIX', 'MDLZ', 'CRM', 'EXC', 'ILMN', 'NI', 'TROW', 'TPR', 'NDAQ', 'GRMN', 'PFG', 'CNP', 'NOC', 'ZBH', 'FIS', 'PRU', 'STX', 'CBRE', 'WLTW', 'ABC', 'MA', 'ANTM', 'CME', 'AAP', 'COP', 'NEM', 'CMCSA', 'XEC', 'KMX', 'WYNN', 'AIZ', 'RF', 'MOS', 'CF', 'EXPE', 'DUK', 'FB', 'UAA', 'VIAB', 'ORCL', 'HBI', 'BLK', 'WU', 'PBCT', 'TEL', 'BK', 'PSA', 'DFS', 'VMC', 'V', 'PM', 'DISCA', 'VRSK', 'IR', 'ACN', 'GM', 'LYB', 'NLSN', 'KMI', 'MPC', 'APTV', 'XYL', 'TRIP', 'CPRI', 'PSX', 'ABBV', 'ETN', 'ZTS', 'NWSA', 'ICE', 'AGN', 'ALLE', 'PRGO', 'SYF', 'QRVO', 'MDT', 'WBA', 'MYL', 'PYPL', 'KHC', 'HPE', 'GOOGL', 'LIN', 'AVGO', 'WRK', 'CI', 'DIS', 'XRX']

dw = pd.DataFrame(w)
dw.columns = ["Ticker Symbol"]

final = pd.merge(dw, g, how="left", on="Ticker Symbol")
df = []

for i in range(final.shape[0]):
    n = []
    n.append(final.iloc[i,0])
    a = data.get_group(final.iloc[i,5])
    gics = a["Ticker Symbol"].tolist()
    gics.remove(final.iloc[i,0])
    r = random.sample(gics, 10)
    for j in range(len(r)):
        n.append(r[j])
    df.append(n)

# "d" is the dataframe contains the sampling result
dsp = pd.DataFrame(df)
c = ["target","sbp1","sbp2","sbp3","sbp4","sbp5","sbp6","sbp7","sbp8","sbp9","sbp10"]
dsp.columns = c

# Import the return information
#r = pd.read_excel("/Users/rachelzheng/Documents/GitHub/bert4search/data/sp500_return.xlsx", sheet_name="WRDS")
r = pd.read_excel("/Users/rachelzheng/Documents/GitHub/bert4search/data/sp500_ret_yrs.xlsx", sheet_name = "WRDS")

time = ["02/28/2017", "03/31/2017", "04/28/2017", "05/31/2017", "06/30/2017","07/31/2017", "08/31/2017", "09/29/2017", "10/31/2017", "11/30/2017", "12/29/2017"]
#time = ["01/31/2018", "02/28/2018", "03/29/2018", "04/30/2018", "05/31/2018", "06/29/2018","07/31/2018", "08/31/2018", "09/29/2018", "10/31/2018", "11/30/2018", "12/31/2018"]

def to_return(select):
    #df1 = pd.merge(dsp[select], rt[["Ticker Symbol", "Returns"]], how='left', left_on=select, right_on="Ticker Symbol")
    #df2 = df1["Returns"]
    df1 = pd.merge(dsp[select], rt[["Ticker Symbol", "Equal-Weighted Return-incl. dividends"]], how='left', left_on=select, right_on="Ticker Symbol")
    df2 = df1["Equal-Weighted Return-incl. dividends"]
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