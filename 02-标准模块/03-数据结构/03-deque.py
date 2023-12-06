# 参考: https://blog.csdn.net/Night__owl/article/details/122709406?spm=1001.2014.3001.5506


# deque
from collections import deque

my_deque = deque()
my_deque.append(1)
my_deque.append(3)
my_deque.append(5)
my_deque.append(7)
my_deque.append(1)

print("原始deque:", my_deque)

# 加入deque尾
my_deque.appendleft(0)
print('加入deque尾一个元素:', my_deque)
print("deque中元素'1'的个数:", my_deque.count(1))

# deque尾弹出一个元素
my_deque.popleft()
print('deque尾弹出一个元素:', my_deque)

# deque反转
my_deque.reverse()
print('deque反转:', my_deque)

# deque长度
print('deque长度:', len(my_deque))