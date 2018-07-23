# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 上午11:41
# @Author  : zhouyajun
import functools


def float_args_and_return(func):
    @functools.wraps(func)  # 此装饰器保证被自定义的装饰器修饰的函数__name__属性值不变
    def wrapper(*args, **kwargs):
        args = [float(arg) for arg in args]
        return float(func(*args, **kwargs))

    return wrapper


@float_args_and_return
def mean(one, second, *rest):
    numbers = (one, second) + rest
    return sum(numbers) / len(numbers)


print(mean.__name__)
