
    # \33[0m 关闭所有属性
    # \33[1m 设置高亮度
    # \33[4m 下划线
    # \33[5m 闪烁
    # \33[7m 反显
    # \33[8m 消隐
    # \33[30m -- \33[37m 设置前景色
    # 字颜色:30-----------37
    # 30:黑
    # 31:红
    # 32:绿
    # 33:黄
    # 34:蓝色
    # 35:紫色
    # 36:深绿
    # 37:白色
 
    # \33[40m -- \33[47m 设置背景色
    # 字背景颜色范围:40----47
    # 40:黑
    # 41:深红
    # 42:绿
    # 43:黄色
    # 44:蓝色
    # 45:紫色
    # 46:深绿
    # 47:白色
    # \33[90m -- \33[97m 黑底彩色
    # 90:黑
    # 91:深红
    # 92:绿
    # 93:黄色
    # 94:蓝色
    # 95:紫色
    # 96:深绿
    # 97:白色
 
    # \33[nA 光标上移n行
    # \33[nB 光标下移n行
    # \33[nC 光标右移n行
    # \33[nD 光标左移n行
    # \33[y;xH设置光标位置
    # \33[2J 清屏
    # \33[K 清除从光标到行尾的内容
    # \33[s 保存光标位置
    # \33[u 恢复光标位置
    # \33[?25l 隐藏光标
    # \33[?25h 显示光标



class ProspectColor:
        black = '\033[90m'
        crimson = '\033[91m'    # 深红
        green = '\033[92m'      # 绿
        yellow = '\033[93m'
        blue = '\033[94m'
        purple = '\033[95m'
        dark_green = '\033[96m' # 深绿
        white = '\033[97m'      # 白色
        clear = '\033[0m'

print('{} 前景: 黑色 {}'.format(ProspectColor.black, ProspectColor.clear))
print('{} 前景: 深红 {}'.format(ProspectColor.crimson, ProspectColor.clear))
print('{} 前景: 绿色 {}'.format(ProspectColor.green, ProspectColor.clear))
print('{} 前景: 黄色 {}'.format(ProspectColor.yellow, ProspectColor.clear))
print('{} 前景: 蓝色 {}'.format(ProspectColor.blue, ProspectColor.clear))
print('{} 前景: 紫色 {}'.format(ProspectColor.purple, ProspectColor.clear))
print('{} 前景: 深绿 {}'.format(ProspectColor.dark_green, ProspectColor.clear))
print('{} 前景: 白色 {}'.format(ProspectColor.white, ProspectColor.clear))

class BackgroundColor:
        black = '\033[40m'
        crimson = '\033[41m'    # 深红
        green = '\033[42m'
        yellow = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        dark_green = '\033[46m'
        white = '\033[47m'
        clear = '\033[0m'

print('{} 背景: 黑色 {}'.format(BackgroundColor.black, BackgroundColor.clear))
print('{} 背景: 深红 {}'.format(BackgroundColor.crimson, BackgroundColor.clear))
print('{} 背景: 绿色 {}'.format(BackgroundColor.green, BackgroundColor.clear))
print('{} 背景: 黄色 {}'.format(BackgroundColor.yellow, BackgroundColor.clear))
print('{} 背景: 蓝色 {}'.format(BackgroundColor.blue, BackgroundColor.clear))
print('{} 背景: 紫色 {}'.format(BackgroundColor.purple, BackgroundColor.clear))
print('{} 背景: 深绿 {}'.format(BackgroundColor.dark_green, BackgroundColor.clear))
print('{} 背景: 白色 {}'.format(BackgroundColor.white, BackgroundColor.clear))


class ProspectColor2:
        black = '\033[30m'
        crimson = '\033[31m'    # 红
        green = '\033[32m'      # 绿
        yellow = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        dark_green = '\033[36m' # 深绿
        white = '\033[37m'      # 白色
        clear = '\033[0m'

print('{} 前景: 黑色 {}'.format(ProspectColor2.black, ProspectColor2.clear))
print('{} 前景: 红色 {}'.format(ProspectColor2.crimson, ProspectColor2.clear))
print('{} 前景: 绿色 {}'.format(ProspectColor2.green, ProspectColor2.clear))
print('{} 前景: 黄色 {}'.format(ProspectColor2.yellow, ProspectColor2.clear))
print('{} 前景: 蓝色 {}'.format(ProspectColor2.blue, ProspectColor2.clear))
print('{} 前景: 紫色 {}'.format(ProspectColor2.purple, ProspectColor2.clear))
print('{} 前景: 深绿 {}'.format(ProspectColor2.dark_green, ProspectColor2.clear))
print('{} 前景: 白色 {}'.format(ProspectColor2.white, ProspectColor2.clear))
