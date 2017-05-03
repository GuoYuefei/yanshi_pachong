#!/usr/bin/python
# coding:utf8
import sys

# 先编写一个登录信息处理的接口，做项目呢得先抽象在实例这样条理才清晰
from abc import abstractmethod, ABCMeta

reload(sys)
sys.setdefaultencoding('utf8')


class IInfoHandle:
    __metaclass__ = ABCMeta  # 指明这是一个抽象类

    @abstractmethod
    def __init__(self):
        pass

    # 根据规律列出username的可能排号
    @abstractmethod
    def parseUsername(self):
        pass

    # 根据规律将password有条理的列出
    @abstractmethod
    def parsePassword(self):
        pass
