#!/bin/sh
python run_pretraining.py \
  --input_file=./data/tf_examples.tfrecord \
  --output_dir=./pretraining_output \
  --do_train=True \
  --do_eval=True \
  --bert_config_file=./bert_config.json \
  --train_batch_size=32 \
  --max_seq_length=100 \
  --max_predictions_per_seq=15 \
  --num_train_steps=10000 \
  --num_warmup_steps=10 \
  --learning_rate=2e-5
