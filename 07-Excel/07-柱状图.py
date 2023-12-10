import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./07-柱状图.xlsx')
students.sort_values(by='Number', inplace=True, ascending=False)
print(students)
# pandas绘图
# students.plot.bar(x='Field', y='Number', color='orange', title='International Students by Field')
plt.bar(students.Field, students.Number, color='orange')
plt.xticks(students.Field, rotation=90)
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students by Field')
# 紧凑型布局
plt.tight_layout()
plt.show()