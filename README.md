# bert4search

This repo is created for the idea using __Bert4Search__ (temp name). The project is trying to bring the state of art from Natural Language Processing, especially the BERT model into the search sequential analysis.

## Local Setup

Tested with Python 3.7 via virtual environment. Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:


```shell
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Data
The data used for this project is EDGAR Log File dataset. It covers the internet search traffic for EDGAR filings through SEC.gov generally covering the period February 14, 2003 through June 30, 2017.  The data is intended to provide insight into the usage of publicly accessible EDGAR company filings in a simple but extensive manner.

EDGAR is the official electronically document submitting system for all public domestic companies in the United States, according to the requirement of SEC. This also provides a platform for investors to look up for the performance of the firms. The log of searching activities from global investors to EDGAR dataset is free to public now, and it provides a valuable source for everyone to study investors' searching behavior.

The official website for EDGAR Log File Dataset is https://www.sec.gov/dera/data/edgar-log-file-data-set.html.  

The explanation for variables can be found at: https://www.sec.gov/files/EDGAR_variables_FINAL.pdf.

## Company
EDGAR identifies company by using the Central Index Key (CIK).

To find a CIK for a company, you can go to the website: https://www.sec.gov/edgar/searchedgar/cik.htm.  

To find a company based on specific CIK, you can use the following website: https://www.sec.gov/edgar/searchedgar/companysearch.html.



## EDA
Go to the eda folder firstly. Then run `$ jupyter notebook` to go over the EDA notebook.


## Data Cleaning

<continue..>


## Search Freuqnecy Count - Using Jan 2017 Data
Count: 217380  

Mean: 17  

25%: 1  

50%: 3  

75%: 6  

Max: 37322
