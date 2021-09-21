import sys
import time
def progress_bar():
    for i in range(1, 101):
        print("\r", end="")
        print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)
progress_bar()

# import time
# scale = 50
# print("执行开始......".center(scale // 2,"-"))
# start = time.perf_counter()
# for i in range(scale + 1):
#     a = "*" * i
#     b = "." * (scale - i)
#     c = (i / scale) * 100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
#     time.sleep(0.1)
# print("\n"+"执行结束".center(scale // 2,"-"))

# 文本进度条简单的开始
# import time
 
# scale = 10
# print("------执行开始------")
# for i in range(scale + 1):
#     a = '*' * i
#     b = '.' * (scale - i)
#     c = (i / scale) * 100
#     print("{:^3.0f}%[{}->{}]".format(c, a, b))
#     time.sleep(0.1)
# print("------执行结束------")

# '''文本进度条单行动态刷新：'''''
# import time
# for i in range(101):
#     print("\r{:3}%".format(i), end="")   # \n 换行   \r  单行显示，定位于最左侧
#     time.sleep(0.1)

# '''文本进度条实例完整效果：'''
 
# import time
 
# scale = 50
# print("执行开始".center(scale // 2, "-"))   # .center 字符串处理方法，将“-”打印在字符串两侧
# start = time.perf_counter()               # perf_counter() 计算时间
# for i in range(scale + 1):
#     a = '*' * i
#     b = '.' * (scale - i)
#     c = (i / scale) * 100
#     dur = time.perf_counter() - start     # 计算打印文本进度条所消耗的时间
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end='')
#     time.sleep(0.1)
# print("\n" + "执行结束".center(scale // 2, '-'))