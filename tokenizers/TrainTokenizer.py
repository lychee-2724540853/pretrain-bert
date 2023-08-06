import docx
from transformers import AutoTokenizer

docs = docx.Document("../data/fault/words/file1.docx")
text = []
for para in docs.paragraphs:
    text.append(para.text)

bertTokenizer = AutoTokenizer.from_pretrained('./bert')

tokenizer = bertTokenizer.train_new_from_iterator(text, 21128)

tokenizer.save_pretrained('./new')