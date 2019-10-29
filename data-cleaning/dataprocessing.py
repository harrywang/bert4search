# This file is created to generate the dataset for model training.
# We've already cleaned the data from the large daily search file from EDGAR.

import numpy as np
import pandas as pd
import datetime

# Define the function to list out the dates in the time period we want.
def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

# Here we use the EDGAR log file from Jan 1, 2017 to Jan 31, 2017.
date = getEveryDay("2017-01-01", "2017-01-31")

for i in range(len(date)):
    d = date[i]
    df = pd.read_csv("/Users/rachelzheng/Documents/GitHub/bert4search/pre-train/data/daily_clean_search/cleaned"+d+".csv")
    df = df.drop(["date","time"],axis=1)
    filename = "search" + d + ".csv"
    unique_ip = df.ip.unique().tolist()
    gk = df.groupby("ip")
    search_seq = []
    for j in range(len(unique_ip)):
        data = gk.get_group(unique_ip[j])
        search_seq.append(list(np.transpose(data["cik"])))
    if i == 0:
        t = pd.DataFrame(search_seq)
        #a = pd.DataFrame(unique_ip)
        #a["date"] = d
        #a = pd.concat([a, t], axis=1)
    else:
        t = pd.concat([t,pd.DataFrame(search_seq)],axis=0)

# t is the dataframe for the search sequence for every ip addresses satisfied the conditions.

l = []
for i in range(t.shape[0]):
    l.append(t.iloc[i,].unique().tolist())

unique_t = pd.DataFrame(l)

for i in range(unique_t.shape[1]):
    name = "search"+str(i)
    if i == 0:
        a = unique_t.iloc[:,i].value_counts().reset_index()
        a.columns = ["cik",name]
    else:
        temp = unique_t.iloc[:,i].value_counts().reset_index()
        temp.columns = ["cik",name]
        a = pd.merge(a,temp,on="cik",how="outer")
a["count"] = a.drop(["cik"],axis=1).apply(lambda x: x.sum(), axis=1)

b = a[a["count"]>200]

# vocab contains 3948 firms which has been searched at least 200 times by different users in a month (Jan 2017).
vocab = b.cik.tolist()

# c gives the training sample which only contains the firm in the "vocab" file.
c = []
for i in range(test.shape[0]):
    a = pd.DataFrame(test.iloc[i,])
    a.columns = ["cik"]
    b = pd.merge(a,v,on="cik",how="inner")
    c.append(b.cik.tolist())
