import pandas as pd

def score_validation(row):
    # 方式1:
    if not 0<= row.Score <= 100:
        print(f'#{row.ID} \t student {row.Name} has an invaild score {row.Score}')
    # 方式2:
    # try:
    #     assert 0<= row.Score <= 100
    # except:
    #     print(f'#{row.ID} \t student {row.Name} has an invaild score {row.Score}')
students = pd.read_excel('./09-数据校验_轴的概念.xlsx')
print(students)
# 轴：
# axis=0: 从上到下排列(列)
# axis=1: 从左到右排列(行)
students.apply(score_validation, axis=1)
