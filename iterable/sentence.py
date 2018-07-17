"""
    迭代模式：一种惰性获取数据的方式，即按需一次获取一个数据项
    所有生成器都得是迭代器，因为生成器实现了迭代器所有的接口
    迭代器用于从集合中取出数据，生成器用于凭空生成数据
    在python中所有集合都是可迭代的
    迭代器用于支持：
        for循环
        构建和扩展集合类型
        逐行遍历文本文件
        列表、字典、集合推导
        元组拆包
        调用函数时，使用*拆包实参
"""


class Sequence:
    ''' 迭代器'''

    def __init__(self):
        pass

    def __next__(self):
        pass

    def __iter__(self):
        pass


import itertools

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, 0.5))
# print(list(gen))


def vowel(c):
    return c.lower() in 'aeiou'

# print(list(itertools.dropwhile(vowel, 'Aoueairidvaouerk')))
# import operator

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        yield 0
        a, b = b, a+b
for i in fibonacci(100):
    print(i)
