# -*- coding: utf-8 -*-
__author__ = 'kholodnyak'
from expenses import *


class BaseGovernment(object):
    """Bazovyj klass, dlja posledujushhej realizacii ierarhii vidov verhovnoj vlasti."""
    _expenses = []
    _type = ""

    @property
    def expenses(self):
        return self._expenses

    def __init__(self, name, number_of_members, greed_level, is_elected, ):
        """

        :param name: Imja vlasti
        :param number_of_members: Kolichestvo chlenov
        :param is_elected: Javljaetsja li vybrannoj
        :param greed_level: Uroven' zhadnosti
        """
        self._name = name
        self._number_of_members = number_of_members
        self._is_elected = is_elected
        self._greed_level = greed_level

    # Popytka sdelat' "kontrakt"
    def get_maintenance_cost(self):
        """Poluchenie stoimosti soderzhanija vlasti"""
        raise NotImplementedError("Please Implement this method")

    def collect_taxes(self):
        """Sobrat' nalogi s naselenija"""
        raise NotImplementedError("Please Implement this method")

    @staticmethod
    def create():
        """Sozdat' ob#ekt tipa vlast'"""
        raise NotImplementedError("Please Implement this method")

    def __str__(self):
        return "Tip vlasti %s. Imja %s. Kolichestvo chlenov %d. Uroven' zhadnosti %f" % (
            self._type, self._name, self._number_of_members, self._greed_level)


class President(BaseGovernment):
    """Tip vlasti Prezidentskaja"""

    def __init__(self, name, greed_level):
        super(President, self).__init__(name, 1, True, greed_level)
        self._type = "Prezidentskaja"
        self._expenses = SecretExpenses(
            VehicleExpenses(
                StaffExpenses(
                    StablingExpenses(
                        RealEstateExpenses(
                            MinimalExpenses()
                        )
                    )
                )
            )
        )

    def get_maintenance_cost(self):
        return self._expenses.get_cost() + (1 + self._greed_level / 100)

    def collect_taxes(self):
        average_tax = 20
        return self._greed_level * average_tax

    @staticmethod
    def create():
        try:
            name = raw_input('Vvedite imja vlasti: ')
            greed_level = int(raw_input('Vvedite uroven zhadnosti vlasti(1-10): '))

            return President(name, greed_level)
        except:
            print 'Nekorrektnye dannye'


class Parlament(BaseGovernment):
    """Tip vlasti Parlamentskaja"""

    def __init__(self, name, number_of_members, greed_level, is_elected):
        super(Parlament, self).__init__(name, number_of_members, greed_level, is_elected)
        self._type = "Parlamentskaja"
        self._expenses = StaffExpenses(
            StaffExpenses(
                VehicleExpenses(
                    RealEstateExpenses(
                        MinimalExpenses()
                    )
                )
            )
        )

    def get_maintenance_cost(self):
        return self._number_of_members * self._expenses.get_cost() + (2 + self._greed_level / 100)

    def collect_taxes(self):
        average_tax = 50
        # Slozhnaja formula sbora nalogov
        return self._greed_level * (average_tax + 10 - self._greed_level * 0.1)

    @staticmethod
    def create():
        try:
            name = raw_input('Vvedite imja vlasti: ')
            number_of_members = int(raw_input('Vvedite kolichestvo chlenov vlasti: '))
            greed_level = int(raw_input('Vvedite uroven zhadnosti vlasti(1-10): '))
            is_elected = bool(raw_input('Javljaetsja li vlast vybrannoj?(0/1): '))

            return Parlament(name, number_of_members, greed_level, is_elected)
        except:
            print 'Nekorrektnye dannye'


class King(BaseGovernment):
    """Tip vlasti "Korolevskaja"""

    def __init__(self, name, greed_level):
        super(King, self).__init__(name, 1, greed_level, False)
        self._type = "Korolevskaja"
        self._expenses = FoolishExpenses(
            MinimalExpenses()
        )

    def get_maintenance_cost(self):
        return self._expenses.get_cost() + (1 - self._greed_level / 150)

    def collect_taxes(self):
        average_tax = 40
        # Osobennyj korolevskij kojefficient
        king_coefficient = 0.98
        return self._greed_level * average_tax * king_coefficient

    @staticmethod
    def create():
        try:
            name = raw_input('Vvedite imja vlasti: ')
            greed_level = int(raw_input('Vvedite uroven zhadnosti vlasti(1-10): '))

            return King(name, greed_level)
        except:
            print 'Nekorrektnye dannye'


class GovernmentCollection(object):
    """Klass, upravljajushhij spiskom ob#ektov tipa Vlast'"""
    CONST_DB_FILE = "governments.db"
    _governments = []

    def __init__(self, governments=None):
        if not (governments is None):
            self._governments = governments

    def __str__(self):
        if 0 == len(self._governments):
            return "Katalog vlastej pust"
        result_str = ""
        counter = 0
        for government in self._governments:
            result_str += str(counter) + ') ' + str(government) + '\n'
            counter += 1
        return result_str

    def add(self, government):
        """Dobavit' pravitel'stvo v spisok"""
        self._governments.append(government)

    def remove(self, id):
        """Udalit' pravitel'stvo po nomeru"""
        if not (0 <= id < len(self._governments)):
            return False

        del self._governments[id]
        return True

    def save_to_file(self, path=CONST_DB_FILE):
        import pickle

        with open(path, 'wb') as output:
            temp_government_collection = GovernmentCollection(self._governments)
            pickle.dump(temp_government_collection, output, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def create_from_file(path=CONST_DB_FILE):
        import pickle

        with open(path, 'rb') as input:
            return pickle.load(input)
