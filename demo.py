# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 上午10:20
# @Author  : zhouyajun

import os

path = '/Users/mac/PycharmProjects/LeetCode'


def print_directory_contents(path):
    for child in os.listdir(path):
        print("===="+child)
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


if __name__ == '__main__':
    print_directory_contents(path)