# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 上午10:04
# @Author  : zhouyajun


def binary_search(sequence, item):
    """
    二分法查找
    :param sequence: 有序序列
    :param item: 待查找元素
    :return: 找到元素返回在序列中索引，找不到返回-1
    """
    low, high = 0, len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sequence[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_smallest(sequence):
    small_index = 0
    smallest_value = sequence[small_index]
    length = len(sequence)
    for i in range(1, length):
        if smallest_value > sequence[i]:
            smallest_value = sequence[i]
            small_index = i
    return small_index, smallest_value


def select_sort(sequence, order='asc'):
    """
    选择排序
    :param sequence: 待排序的序列
    :param order: 排序方式
    :return:
    """
    new_sequence = []
    for i in range(len(sequence)):
        small_index, smallest_value = find_smallest(sequence)
        if order == 'asc':
            new_sequence.insert(0, smallest_value)
        else:
            new_sequence.append(smallest_value)
        sequence.pop(small_index)
    return new_sequence


def quick_sort(sequence):
    """
    快速排序
    :param sequence:
    :return:
    """
    if len(sequence) < 2:
        return sequence
    else:
        pivor = sequence[0]  # 给定基准值
        pivor_left = [i for i in sequence if i < pivor]  # 将小于基准值的放到基准值的左边，新建一个列表
        pivor_right = [i for i in sequence if i > pivor]  # 将大于基准值的放到基准值的右边，新建列表
        return quick_sort(pivor_left) + [pivor] + quick_sort(pivor_right)


def length(sequence):
    if not sequence:
        return 0
    sequence.pop()
    return 1 + length(sequence)


def max_value(sequence):
    if len(sequence) == 0:
        return None
    elif len(sequence) == 1:
        return sequence[0]
    else:
        return sequence[0] if sequence[0] > max_value(sequence[1:]) else max_value(sequence[1:])


if __name__ == '__main__':
    sequence = [1, 4, 6, -1, 6, 0, 23, 5, 6, 1]
    print(max_value(sequence))
