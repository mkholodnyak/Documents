# -*- coding: utf8 -*-
__author__ = 'kholodnyak'

from kholodnyak import *
from kholodnyak.tasks import *
from kholodnyak.parser import *


def call_func(function_name, args=''):
    eval(function_name + '(' + args + ')')


def main():
    while True:
        task_number = raw_input('Vvedite nomer zadachi (1-16): ')

        if not Parser.try_parse(task_number):
            print 'Oshibka vvoda nomera!'
            continue

        task_number = int(task_number)
        if 0 == task_number:
            print 'Vveden nol'. Zavershaem programmu'
            break
        if not (task_number in range(1, 17)):
            print 'Vyshli za granicy intervala'
            continue
        try:
            call_func('Task' + str(task_number))
        except SuperException as exc:
            print exc.ErrorMessage
        except BaseException:
            print 'Srabotalo iskljuchenie!'


main()