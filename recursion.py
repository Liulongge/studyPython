def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

number = int(input("请输入一个正整数： "))
result = factorial(number)
print("%d 的阶乘为： %d" %(number, result))



def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)

number = int(input("请输入一个正整数： "))
result = factorial(number)
print("%d 的阶乘为： %d" %(number, result))