import os
import docx
from transformers import AutoTokenizer

path = "../data/fault/txt"
filelist = os.listdir(path)
text = []
for file in filelist:
    file = open(os.path.join(path, file), 'r', encoding='utf8')
    for line in file:
        line = line.strip()
        if len(line) > 1:
            text.append(line)

bertTokenizer = AutoTokenizer.from_pretrained('./bert')

tokenizer = bertTokenizer.train_new_from_iterator(text, 21128)

tokenizer.save_pretrained('./new')