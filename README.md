# 预训练BERT
## 一、主要过程
    1. 训练数据准备和预处理
    2. 创建tokenizer
    3. 训练模型

## 二、训练数据准备和预处理

现在的代码将所有训练文本归在一个文件中，分为train.txt, valid.txt, test.txt
每个txt中包含所有文档的内容，每一行一个paragraph。

考虑到所有原始数据是docx/doc格式，因此需要把所有docx/doc转换为txt
