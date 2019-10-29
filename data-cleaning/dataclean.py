# This file is created to clean the data and provide the datafile satisfied for the BERt pre-training step.

import numpy as np
import pandas as pd
import datetime

# Here we use the EDGAR Log File from Jan 01, 2017 to Jan 31, 2017.
def getEveryDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

date = getEveryDay("2017-01-01", "2017-01-31")

# Import the file

# Using the result from the EDA report, we limit the observation by the following restrictions:
# 1. IP needs to identify itself as not the crawler (crawler = 0).
# 2. IP cannot search for more than 100 times per day.
# 3. IP needs to search at least 3 times per day.

for i in range(len(date)):
    raw = pd.read_csv("/Volumes/Untitled/Summer Paper/log2017data/data/log"+str(date[i])+".csv")
    #raw = pd.read_csv("/Users/rachelzheng/Documents/GitHub/bert4search/eda/log"+str(date[0])+".csv")
    file_name = "cleaned" + str(date[i]) + ".csv"
    gk = raw[raw["crawler"] == 0].groupby("ip")
    unique_ip = raw[raw["crawler"] == 0].ip.unique()

    search_seq = []
    for i in range(len(unique_ip)):
        data = gk.get_group(unique_ip[i])
        search_seq.append(list(np.transpose(data["cik"])))

    freq = []
    for i in range(len(search_seq)):
        freq.append(len(search_seq[i]))
    b = pd.DataFrame(freq)
    c = pd.concat([pd.DataFrame(unique_ip), b], axis=1)
    c.columns = ["ip", "Frequency"]

    final_ip = pd.DataFrame(c[(c["Frequency"] <= 100) & (c["Frequency"] >= 3)].ip)
    final_ip.columns = ["ip"]

    search = pd.merge(final_ip, raw[raw["crawler"] == 0], left_on="ip", right_on="ip", how="inner").drop(
        ['zone', 'accession', 'extention', 'code', 'size', 'idx', 'norefer', 'noagent', 'find', 'crawler', 'browser'],
        axis=1)

    #search.to_csv(file_name,index=None)







