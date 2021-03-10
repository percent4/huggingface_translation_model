# -*- coding: utf-8 -*-
# @Time : 2021/2/8 11:13
# @Author : Jclian91
# @File : zh_en_mt.py
# @Place : Yangpu, Shanghai
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("./opus-mt-zh-en")

model = AutoModelForSeq2SeqLM.from_pretrained("./opus-mt-zh-en")

text = "从时间上看，中国空间站的建造比国际空间站晚20多年。"
# Tokenize the text
batch = tokenizer.prepare_seq2seq_batch(src_texts=[text])

# Make sure that the tokenized text does not exceed the maximum
# allowed size of 512
batch["input_ids"] = batch["input_ids"][:, :512]
batch["attention_mask"] = batch["attention_mask"][:, :512]

# Perform the translation and decode the output
translation = model.generate(**batch)
result = tokenizer.batch_decode(translation, skip_special_tokens=True)
print(result)