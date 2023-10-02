#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Project : advanced
# @File : 01.py
# @Author : Yu Zhang
# @Date : 2023/10/2 16:43

# 01 类和实例

# 02 访问限制
"""
1.__xxx___，是特殊变量，它是可以直接访问的，不是private变量。
"""

# 03 继承和多态
"""
1.定义一个class时，实际上就定义了一种数据类型。
2.动态语言的"鸭子类型"，它并不要求严格的继承体系，一个对象只要"看起来像鸭子，走起路来像鸭子"，那它就可以被看做是鸭子。
3.仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态。
"""

# 04 实例属性和类属性



# 04 获取对象信息
class Animal:
    def __init__(self):
        pass


class Dog(Animal):
    def __init__(self):
        super().__init__()


class Husky(Dog):
    def __init__(self):
        super().__init__()


def t1():
    h = Husky()
    d = Dog()
    a = Animal()

    print(type(h) == type(d))
    print(isinstance(h, Animal))


if __name__ == '__main__':
    t1()
