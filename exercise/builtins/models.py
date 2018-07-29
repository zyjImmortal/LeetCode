import itertools

a = itertools.count(10, 2)
print(a)

# takewhile 返回一个生成器，同时入参是一个过滤条件和一个生成器
b = list(itertools.takewhile(lambda n: n < 20, itertools.count(1, 2)))
print(b)
