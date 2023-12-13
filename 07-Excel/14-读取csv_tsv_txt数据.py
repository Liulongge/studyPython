import pandas as pd
# TSV 是Tab-separated values的缩写，即制表符分隔值。
# CSV，Comma-separated values（逗号分隔值）更常见一些。

# TSV与CSV的区别： 
# 1）从名称上即可知道，TSV是用制表符（Tab,'\t'）作为字段值的分隔符；
# CSV是用半角逗号（','）作为字段值的分隔符； 
# 2）IANA规定的标准TSV格式，字段值之中是不允许出现制表符的。
# Python对TSV文件的支持： 
# Python的csv模块准确的讲应该叫做dsv模块，因为它实际上是支持范式的分隔符分隔值文件
# （DSV，delimiter-separated values）的。 delimiter参数值默认为半角逗号，即默认将被处理文件视为CSV。 
# 当delimiter='\t'时，被处理文件就是TSV。

students1 = pd.read_csv('14-读取csv_tsv_txt数据.csv', index_col='ID')
print('csv格式数据:\n',students1)

students2 = pd.read_csv('14-读取csv_tsv_txt数据.tsv', sep='\t')
print('tsv格式数据:\n',students2)

# sep='|': 表示使用'|'作为分割
students3 = pd.read_csv('14-读取csv_tsv_txt数据.txt', sep='|', index_col='ID')
print('txt格式数据:\n',students3)