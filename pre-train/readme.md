# bert4search

## Pre-Training

The pre-training step is learned from the design of the Bidirectional Encoder Representations from Transformers (BERT). Here is the link for the official BERT repo: https://github.com/google-research/bert.  

The data (__search.txt__) for this step can be found at: https://drive.google.com/file/d/1ZMNM0RtNZVJ5fT3xwNX92PPJ5D_0ERm8/view?usp=sharing.
The input is a plain text file, with one sequence per line, which represents the daily search sequence from one IP address. Different search sequences from different IP address or different days are delimited by empty lines. 

__Note__: Please note that here the search sequence only contains the 3948 companies which are identified in previous data cleaning firms. Those companies have been searched at least 200 times in January 2017 by different IP addresses.  

Here's how to run the pre-training. Do not include init_checkpoint if you are pre-training from scratch. The model configuration (including vocab size) is specified in ```bert_config_file```. The max_seq_length and max_predictions_per_seq parameters passed to __run_pretraining.py__ must be the same as __create_pretraining_data.py__. The __max_predictions_per_seq__ is the maximum number of masked LM predictions per sequence. You should set this to around __max_seq_length__ * __masked_lm_prob__.

### Local Setup
To run this program, you need to set up the required package in your local folder (__bert_pretrain__ folder) firstly.  

```shell
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Before you go into the next two steps, it is necessary to make ```run.txt``` and ```run_pretrain.txt``` files executable.

### Step 1. Data Generation
The output is a set of __tf.train.Examples__ serialized into __TFRecord__ file format.
```shell
./run.txt
```

### Step 2. Pre-Training
The pre-training here will train the model in two tasks: __Masked LM__ task and __Next Sentence Prediction__ task. Here we don't rely the result for __Next Sentence Prediction__ for this moment.
```shell
./run_pretrain.txt
```

The expected output will be like:
```shell
***** Eval results *****
global_step = 5000
loss = 2.469844
masked_lm_accuracy = 0.69673204
masked_lm_loss = 2.4894028
next_sentence_accuracy = 1.0
next_sentence_loss = 1.3851975e-05
```
