#!/usr/bin/env python3
# coding: utf-8
# @Time : 2021/2/8 11:28
# @Author : Jclian91
# @File : en_zh_mt.py
# @Place : Yangpu, Shanghai
# import shap
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("./opus-mt-en-zh")

# model = AutoModelForSeq2SeqLM.from_pretrained("./opus-mt-en-zh")

# text = "In terms of time, the Chinese space station was built more than 20 years later than the International Space Station."
# # Tokenize the text
# batch = tokenizer.prepare_seq2seq_batch(src_texts=[text])

# # Make sure that the tokenized text does not exceed the maximum
# # allowed size of 512
# batch["input_ids"] = batch["input_ids"][:, :512]
# batch["attention_mask"] = batch["attention_mask"][:, :512]

# # Perform the translation and decode the output
# translation = model.generate(**batch)
# result = tokenizer.batch_decode(translation, skip_special_tokens=True)
# print(result)

from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
res=translator("我想吃苹果")
print(res)

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
res=translator("There will be many numbers and statistics in this video that may shock or even scare you, but the point is not to discourage you or anyone working to clean up this stuff from our oceans, beaches, rivers, and backyards.")
print(res)
