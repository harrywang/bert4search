# Pre-Training

This folder is created for applying the pre-training method in the bert4search project.

## Data

To pre-train the model, we use the data from Jan 01, 2017 to Feb 28, 2017. To apply the analysis result from EDA report, basic data cleaning is required.  

The data cleaning steps include:  

1. Restrict to the ip who needs to identify itself not as crawler (crawler=0).  

2. Restrict to the ip who needs to search less than 100 times in the particular day.  

3. Restrict to the ip who needs to search at least 3 times in the particular day.

The row of the final after-clean dataset for retraining represents the daily search activity of the ip which satisfies all data cleaning conditions.

To better apply the BERT into this project, the searched companies are restricted to the top 30000 frequent searched firms using the final after-clean dataset. For each row of the after-clean dataset, the duplicate search for one company will be count as 1. Using the unique search count for each firm (cik-based) could identify the top 30000 frequent search firms.
