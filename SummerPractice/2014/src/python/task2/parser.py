__author__ = 'kholodnyak'

import kholodnyak as lib


class Parser(object):
    @staticmethod
    def try_parse(obj, to_type='int'):

        allowed_types = ['int', 'float']
        if not (to_type in allowed_types):
            return False

        try:
            lib.call_func(to_type, str(obj))
            return True
        except:
            return False