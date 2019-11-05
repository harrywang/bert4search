# bert4search

## Pre-Training

The pre-training step is learned from the design of the Bidirectional Encoder Representations from Transformers (BERT). Here is the link for the official BERT repo: https://github.com/google-research/bert.  

Here's how to run the pre-training. Do not include init_checkpoint if you are pre-training from scratch. The model configuration (including vocab size) is specified in bert_config_file. The max_seq_length and max_predictions_per_seq parameters passed to run_pretraining.py must be the same as create_pretraining_data.py. The max_predictions_per_seq is the maximum number of masked LM predictions per sequence. You should set this to around max_seq_length * masked_lm_prob.

### Data

The data (__search-log-jan-2017.txt__) for this step can be found at: https://drive.google.com/file/d/1ZMNM0RtNZVJ5fT3xwNX92PPJ5D_0ERm8
The input is a plain text file, with one sequence per line, which represents the daily search sequence from one IP address from Jan 1, 2017 to Jan 31, 2017. Different search sequences from different IP address or different days are delimited by empty lines.

****Optional****
Run `$ wc -l search.txt` to find out the total number of lines in the file, which is 744,413. This file is quite big and you can split it into smaller files with 100,000 lines each by using Linux version of `split`.

```
$ brew install coreutils
$ gsplit -a 4 -d -l 10000 search.txt search_
```


Download the txt file and put in the /pre-train/data folder and rename to `search.txt`

__Note__: Please note that here the search sequence only contains the 3948 companies which are identified in previous data cleaning firms. Those companies have been searched at least 200 times in January 2017 by different IP addresses.  

### Local Setup
To run this program, you need to set up the required package in your local folder (__bert_pretrain__ folder) firstly.  

```shell
$ python3.7 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Step 1. Data Generation
The output is a set of __tf.train.Examples__ serialized into __TFRecord__ file format. 
```shell
chmod +x run.sh
./run.sh
```

### Step 2. Pre-Training
The pre-training here will train the model in two tasks: __Masked LM__ task and __Next Sentence Prediction__ task. Here we don't rely the result for __Next Sentence Prediction__ for this moment.
```shell
chmod +x run_pretrain.sh
./run_pretrain.sh
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
