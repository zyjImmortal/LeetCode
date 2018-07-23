# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午10:39
# @Author  : zhouyajun

import abc
import collections
import sys
import textwrap
import html

class Renderer(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasscheck__(cls, subclass):
        if cls is Renderer:  # 判断当前类是不是基类，如果不是，则抛出错误，表明子类不可以继承这个行为
            # __mro__方法返回类的继承解析顺序，以列表的形式包含所有继承的类，__dict__返回类的所有方法和属性与对应的值，以字典的形式
            # ChainMap把多个字典映射到一个字典
            attributes = collections.ChainMap(*(SupperClass.__dict__ for SupperClass in subclass.__mro__))
            methods = ('header', 'paragraph', 'footer')
            # all归约函数，所有都为True，才返回True
            if all(method in attributes for method in methods):
                return True
        return NotImplementedError


class TextRenderer(Renderer):
    def __init__(self, width=80, file=sys.stdout):
        self.width = width
        self.file = file
        self.previous = False

    def header(self, title):
        self.file.write('{0:^{2}}\n{1:^{2}}\n'.format(title, '=' * len(title), self.width))

    def paragraph(self, text):
        if self.previous:
            self.file.write('\n')
        self.file.write(textwrap.fill(text, self.width))
        self.file.write('\n')
        self.previous = True

    def footer(self):
        pass


class HtmlWriter:

    def __init__(self, file=sys.stdout):
        self.file = file

    def header(self):
        self.file.write('<!doctype html>\n<html>\n')

    def title(self, title):
        self.file.write('<head><title>{}</title></head>\n'.format(html.escape(title)))

    def start_body(self):
        self.file.write('<body>\n')

    def body(self, text):
        self.file.write('<p>{}</p>\n'.format(html.escape(text)))

    def end_body(self):
        self.file.write('<>')


class HtmlRenderer:
    pass


class Page:
    def __init__(self, title, renderer):
        if not isinstance(renderer, Renderer):
            raise TypeError('Expected object of type Rnderer, got {}'.format(type(renderer).__name__))
        self.title = title
        self.renderer = renderer
        self.paragraphs = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()
