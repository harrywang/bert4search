# This file is created to generate the dataset for model training.
# We've already cleaned the data from the large daily search file from EDGAR.

import numpy as np
import pandas as pd

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

for i in range(len(date)):
    if i == 0:
        df = pd.read_csv("/Users/rachelzheng/Documents/GitHub/bert4search/pre-train/data/daily_clean_search/cleaned"+date[i]+".csv ")
        

