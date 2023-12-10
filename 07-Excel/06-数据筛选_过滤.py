import pandas as pd

def age_18_to_30(a):
    return 18 <= a < 30

def level_a(s):
    return 85 <= s <= 100
    
students = pd.read_excel('./06-数据筛选_过滤.xlsx', index_col='ID')
students = students.loc[students['Age'].apply(age_18_to_30)]
print('筛选年龄在18-30的学生:\n',students)
students = students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]
# 高级语法
# students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]
# 使用lambda表达式
# students = students.loc[students.Age.apply(lambda a:18 <= a < 30)] \
#     .loc[students.Score.apply(lambda s:85 <= s <= 100)]
print('筛选年龄在18-30同时成绩再85-100的学生:\n',students)