# -*- coding: utf-8 -*-
# @Time    : 2018/4/4 下午1:16
# @Author  : zhouyajun


from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decoratord(*args, **kwargs):
        if not can_run:
            return "not running!"
        return f(*args, **kwargs)
    return decoratord
can_run = True
@decorator_name
def func():
    print("runnng!1")

print(func())