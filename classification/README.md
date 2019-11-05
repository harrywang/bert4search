# bert4search

## Classification Task  

This part is to use the pre-training result to find the top 10 related firms for each target firm.


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