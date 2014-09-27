# -*- coding: utf8 -*-
__author__ = 'kholodnyak'


class SuperException(BaseException):
    def __init__(self, message):
        self.ErrorMessage = message


def call_func(function_name, args=''):
    eval(function_name + '(' + args + ')')