# Python处理Excel的好处
## 批量处理
        当要处理十几个Excel文件时，用Python可以实现批量扫描、自动化处理，替代手工重复处理Excel
## 大型文件
        文件超过十几MB时，用Excel打开和处理开始变慢，Python可以处理更大的文件
## Python易学强大
        相比过时复杂的VBA，Python简单易学，并且能处理各种复杂的业务逻辑
## Python庞大生态圈
        使用Python，可以结合爬虫、web服务、MySQL、Word、定时任务、人工智能等更多扩展功能

# Python处理Excel类库总结
## 三大开源库Pandas、openpyxl、xlwings
        90%情况，用Pandas一个库就可以搞定
        如果想要控制格式、样式，可以用Pandas配合两个库：
        1、如果是Windows、Mac可以结合xlwings，更强大
        2、如果是Linux或者系统没有安装Office，用openpyxl(相比于xlwings弱一些)
## 如虎添翼的其他类库
        爬虫: requsts/bs4
        Web网页: flask
        数据可视化: Matplotlib
        机器学习: SkLearn
        与Word互通: python-docx
        发送邮件: smtplib