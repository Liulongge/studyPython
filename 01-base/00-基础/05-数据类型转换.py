
x = 3
# int(x)类型: <class 'int'>, 3
# float(x)类型: <class 'float'>, 3.0
# str(x)类型: <class 'str'>, 3
# chr(x)类型: <class 'str'>, 
# hex(x)类型: <class 'str'>, 0x3
# 八进制 otc(x)类型: <class 'str'>, 0o3
# 二进制 bin(x)类型: <class 'str'>, 0b11
print('int(x)类型: {}, {}'.format(type(int(x)), int(x)))
print('float(x)类型: {}, {}'.format(type(float(x)), float(x)))
print('str(x)类型: {}, {}'.format(type(str(x)), str(x)))
print('chr(x)类型: {}, {}'.format(type(chr(x)), chr(x)))
print('hex(x)类型: {}, {}'.format(type(hex(x)), hex(x)))
print('otc(x)类型: {}, {}'.format(type(oct(x)), oct(x)))
print('bin(x)类型: {}, {}'.format(type(bin(x)), bin(x)))

