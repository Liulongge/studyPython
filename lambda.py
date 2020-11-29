g = lambda x : 2 * x + 1
print(g(2))


g = lambda x, y : x + y
print(g(2,3))


def odd(x):
    return x % 2
temp = range(10)
show = filter(odd, temp)
print(list(show))

m = list(filter(lambda x : x % 2 , range(10)))
print(m)