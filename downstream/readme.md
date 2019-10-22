# bert4search

## Downstream Task

The downstream task is to check if the top 10 related firms are in the same industrial classification.  

Here we use "bert-as-service" to find the top related firms.  

The details for this tool can be found at the official repo: https://github.com/hanxiao/bert-as-service.  

You may need to install the server and client firstly.  

```shell
pip install bert-serving-server # server
pip install bert-serving-client # client
```

## Getting Started 

1. Prepare the pre-trained model.  

You need to have the pre-trained model at this step.  

2. Start the BERT services. 

You can start the tool as follows:  

```shell
bert-serving-start -model_dir /tmp/pretrain4search/ -num_worker=1
```

## Industrial Classification Information. 

There are three types of most common industrial classification standards:  

1. __SIC__ (Standard Industrial Classification). 

2. __NAICS__ (North American Industry Classification System). 

3. __GICS__ (Global Industry Classification Scheme). 


The details of these three can be found online. In this paper, the classification information towards each company is collected through __Compustat - Capital IQ__ on Wharton Research Data Services (WRDS).  

 



