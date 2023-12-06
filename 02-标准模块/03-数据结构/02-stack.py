

# 用列表实现栈在前面的list部分已经提到了，这里给出样例
stack = [1,4,5,6,3,2]
print("原始stack: {}".format(stack))

for i in range(2):
    stack.pop()
print("pop两个元素后stack: {}".format(stack))

# 按下标出栈
print("按下标'1'出栈: {}".format(stack.pop(1)))
print("出栈后stack: {}".format(stack))

# 栈顶
print("栈顶: {}".format(stack[-1]))
