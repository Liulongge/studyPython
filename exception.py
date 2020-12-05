try:
    f = open("我为什么是一个文件.txt")
    print(f.read())
    f.close()
except OSError:
    print("文件出错啦T_T")

try:
    f = open("我为什么是一个文件.txt")
    print(f.read())
    f.close()
except OSError as reason:
    print("文件出错啦T_T, 原因是：" + str(reason))

try:
    sum = 1 + "1"
    f = open("我为什么是一个文件.txt")
    print(f.read())
    f.close()
except OSError as reason:
    print("文件出错啦T_T, 原因是：" + str(reason))
except TypeError as reason:
    print("类型出错啦T_T, 原因是：" + str(reason))


try:
    sum = 1 + "1"
    f = open("我为什么是一个文件.txt")
    print(f.read())
    f.close()
except :
    print("出错啦T_T")

try:
    sum = 1 + "1"
    f = open("我为什么是一个文件.txt")
    print(f.read())
    f.close()
except (OSError, TypeError):
    print("出错啦T_T")


try:
    f = open("我为什么是一个文件.txt")
    print(f.read())
    sum = 1 + "1"
    f.close()
except (OSError, TypeError):
    print("出错啦T_T")
finally:
    f.close()
    print("f.close")

