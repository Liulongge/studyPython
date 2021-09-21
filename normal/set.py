set1 = {1,2,7,8,8,8,8,8}
print(set1)

set2 = set([1,2,7,8,8,8,8,8])
print(set2)

#### 去除集合中重复元素 ####
num1 = [1,2,3,4,5,5,3,1,0]
print("集合：", num1)
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)

print("去除集合中重复元素, 方法1：",temp)

num2 = list(set(num1))
print("去除集合中重复元素，方法2：",num2)