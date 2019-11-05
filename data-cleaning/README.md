# bert4search

##  Pre-Training

This folder is created for applying the pre-training method in the bert4search project.

## Data

To pre-train the model, we use the data from Jan 01, 2017 to Jan 31, 2017. To apply the analysis result from EDA report, basic data cleaning is required.  

## Data Cleaning

The data cleaning steps include:  

1. Restrict to the ip who needs to identify itself not as crawler (crawler=0).  

2. Restrict to the ip who needs to search less than 100 times in the particular day.  

3. Restrict to the ip who needs to search at least 3 times in the particular day.

The row of the final after-clean dataset for retraining represents the daily search activity of the ip which satisfies all data cleaning conditions.

To better apply the BERT into this project, the searched companies are restricted to the top frequent searched firms using the final after-clean dataset. For each row of the after-clean dataset, the duplicate search for one company will be count as 1. Using the unique search count for each firm (cik-based) could identify the top frequent search firms.

To select the top frequent searched firms, we firstly count the frequency of unique firms for each search sequence from satisfied IP address. Based on the distribution of the searched frequency, we select the top 3948 frequent firms, which have been searched at least 200 times.  This gives us the "vocabulary" to learn.  

Once we have the "vocab" file, we replace the original search sequences with the new sequence only with the firms in the "vocab" file.  This gives us the training sample for the proposed model.  

## Get Start

Because of the memory limit and the large size of the original daily EDGAR log file, we have two steps to clean the data. The ```dataclean.py``` file cleans the original daily search Log file and the ```dataprocessing.py``` generates the input file for next pre-training step. 

### Local Setup
```shell
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Step 1.Data Clean

In the first step, we clean the daily search file and keep the observations satisfied the conditions.  
```shell
$ python3 dataclean.py
```

### Step 2. Data Generation
In the second step, we use the cleaned daily search files to generate the input file for pre-training step.
```shell
$ python3 dataprocessing.py
```

