# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午9:44
# @Author  : zhouyajun

"""
python创建对象的几种方式
"""
import sys
import copy


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)


# point1 = Point(3, 4)  # 静态创建，其余动态创建，3，4， 7比较优雅的方式
# print('point1--->', id(point1))
# point2 = eval('{}({},{})'.format('Point', 4, 5))
# print('point2---->', id(point2))
# point3 = getattr(sys.modules[__name__], 'Point')(5, 6)
# print('point3--->', id(point3))
# point4 = globals()['Point'](6, 7)
# print('point4------>', id(point4))
# point5 = make_object(Point, 7, 8)
# print('point5---->', id(point5))
# point6 = copy.deepcopy(point1)
# point6.x = 8
# point6.y = 9
# print('point6----->', id(point6))
# point7 = point1.__class__(9, 1)啊=
# print('point7---->', id(point7))
print(globals())