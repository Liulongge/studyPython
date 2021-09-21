count = 10
def myFunc():
    count = 5;
    print(count)

myFunc()
print(count)


count = 10
def myFunc():
    global count
    count = 5;
    print(count)

myFunc()
print(count)

def func1():
    print("func1 正在被调用")
    def func2():
        print("func2 正在被调用")
    func2()

func1()

#### 闭包 ####
def funcA():
    x = 5
    def funcB():
        nonlocal x
        x *= x
        return x
    return funcB()

print(funcA())