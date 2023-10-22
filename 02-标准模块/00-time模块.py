import time


print(time.localtime(time.time()).tm_year,
        '/', time.localtime(time.time()).tm_mon,
        '/', time.localtime(time.time()).tm_mday,
        'hour: ',time.localtime(time.time()).tm_hour,
        'min: ',time.localtime(time.time()).tm_min,
        's: ', time.localtime(time.time()).tm_sec,
        '周几: ', time.localtime(time.time()).tm_wday,
        '第几天: ',time.localtime(time.time()).tm_yday,
        '夏令时: ', time.localtime(time.time()).tm_isdst)

# 1. time()
# time函数用于返回当前时间的时间戳，格林尼治时间到现在的秒数。
print('time.time(): ', time.time()) #1661868092.4191587

# 2. localtime()
# 该函数是将时间戳格式化为本地时间，返回struct_time对象。
# 它有一个参数用于接收时间戳，如果调用函数时不提供时间戳（注意是提供秒数），它会默认使用当前时间戳。
print('localtime(): ', time.localtime())
# time.struct_time(tm_year=2023, tm_mon=10, tm_mday=23, tm_hour=0, tm_min=57, tm_sec=27, tm_wday=0, tm_yday=296, tm_isdst=0)

# 如果提供0的时间戳，它返回的就恰好是那个格林尼治时间。同时它返回的也是struct_time类型。
print('localtime(): ', time.localtime(0))
# time.struct_time(tm_year=2023, tm_mon=10, tm_mday=23, tm_hour=0, tm_min=57, tm_sec=27, tm_wday=0, tm_yday=296, tm_isdst=0)

# 3. mktime()
# 它接收struct_time对象作为参数，它返回的是用秒数来表示时间的浮点数
# （该浮点数小数后面全是0，前面time.time()返回的浮点数小数后面就不全为0），
# 就是从格林尼治时间到某年某月某日某时某分某秒的秒数。它的参数可以是结构化的时间。
print('mktime(): ', time.mktime(time.localtime())) # 1697993847.0
print('mktime(): ', time.localtime(time.mktime(time.localtime())))
# time.struct_time(tm_year=2023, tm_mon=10, tm_mday=23, tm_hour=0, tm_min=57, tm_sec=27, tm_wday=0, tm_yday=296, tm_isdst=0)

# 4. gmtime()
# 它能将一个时间戳转换为UTC的struct_time，参数为时间戳，默认参数为当前时间戳（也就是time.time()）。
# UTC，协调世界时，也叫世界标准时间，它是以原子时秒长在时刻上尽量接近于世界时的一种时间计量系统。
print('gmtime(): ', time.gmtime())
# time.struct_time(tm_year=2023, tm_mon=10, tm_mday=22, tm_hour=16, tm_min=59, tm_sec=46, tm_wday=6, tm_yday=295, tm_isdst=0)
print('gmtime(): ', time.gmtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# 5. asctime()
# 它接收时间元组并返回一个形式为“Tue Aug 30 22:36:35 2022 ”的24个字符的字符串（空格也要算）。
# 它接收的参数可以是时间元组也可以是time_struct对象。
a = (2022,8,30,22,36,35,1,1,0)
print('asctime(): ', time.asctime(a))
#Tue Aug 30 22:36:35 2022
print('asctime(): ', time.asctime(time.localtime()))
# Mon Oct 23 01:01:43 2023