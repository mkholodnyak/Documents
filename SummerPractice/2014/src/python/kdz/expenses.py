# -*- coding: utf-8 -*-
__author__ = 'kholodnyak'


class BaseExpenses(object):
    """Bazovyj klass dlja posledujushhej realizacii naslednikov Rashody"""

    _description = ""

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def get_cost(self):
        """Poluchit' stoimost' soderzhanija vlasti"""
        raise NotImplementedError("Please Implement this method")


class MinimalExpenses(BaseExpenses):
    """Minimal'nye rashody, nezavisimye ot tipa vlasti"""

    def __init__(self):
        self._description = "Minimal'nye rashody"

    def get_cost(self):
        return 50


# Realizacija patterna dekorator dlja klassa Rashodov
class ExpensesDecorator(BaseExpenses):
    _expenses = BaseExpenses()

    def __init__(self, expenses):
        self._expenses = expenses


class RealEstateExpenses(ExpensesDecorator):
    """Sovokupnaja stoimost' dvorcov i rezidencij"""

    def __init__(self, expenses):
        super(RealEstateExpenses, self).__init__(expenses)
        self._description = self._expenses.description + " , nedvizhimost'"

    def get_cost(self):
        return self._expenses.get_cost() + 75


class StaffExpenses(ExpensesDecorator):
    """Zatraty na personal(ohranu)"""

    def __init__(self, expenses):
        super(StaffExpenses, self).__init__(expenses)
        self._description = self._expenses.description + ", zatraty na personal"

    def get_cost(self):
        return self._expenses.get_cost() + 35


class StablingExpenses(ExpensesDecorator):
    """Zatraty na konjushnju"""

    def __init__(self, expenses):
        super(StablingExpenses, self).__init__(expenses)
        self._description = self._expenses.description + ", zatraty na konjushnju"

    def get_cost(self):
        return self._expenses.get_cost() + 25


class VehicleExpenses(ExpensesDecorator):
    """Sovokupnaja stoimost' a\m i samoletov"""

    def __init__(self, expenses):
        super(VehicleExpenses, self).__init__(expenses)
        self._description = self._expenses.description + ", sredstva peredvizhenija"

    def get_cost(self):
        return self._expenses.get_cost() + 40


class SecretExpenses(ExpensesDecorator):
    """Sekretnaja stat'ja rashodov"""
    def __init__(self, expenses):
        super(SecretExpenses, self).__init__(expenses)
        self._description = self._expenses.description + ", sekretnye rashody"

    def get_cost(self):
        return self._expenses.get_cost() + 105


class FoolishExpenses(ExpensesDecorator):
    """Razlichnye rashody na prihoti vlasti(v nashem sluchae - korol')"""
    def __init__(self, expenses):
        super(FoolishExpenses, self).__init__(expenses)
        self._description = self._expenses.description + ", razlichnye prihoti"

    def get_cost(self):
        return self._expenses.get_cost() + 160