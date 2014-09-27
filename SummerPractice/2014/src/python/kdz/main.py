# -*- coding: utf-8 -*-
__author__ = 'kholodnyak'

from components.governments import *


class InputHandler(object):
    def __init__(self):
        self._government_collection = GovernmentCollection()


    def print_hint(self):
        print """
Vyberite komandu iz spiska:
    1 — Vyvesti spisok vlastej na jekran
    2 — Dobavit' zapis' v katalog
    3 — Udalit' zapis' iz kataloga
    4 — Sohranit' katalog v fajl
    5 — Sozdat' katalog iz fajla
    0 — Zakryt' programmu
        """

    def print_catalog(self):
        print self._government_collection

    def add_government(self):
        print """
Vyberite tip pravitel'stva:
1 — Prezident
2 — Parlament
3 — Korol'
        """
        try:
            government_type = int(raw_input('>>>'))
            if not (government_type in range(1, 3 + 1)):
                raise Exception()
            # TODO: Sdelat' fabriku
            if 1 == government_type:
                government = President.create()
            elif 2 == government_type:
                government = Parlament.create()
            else:
                government = King.create()

            self._government_collection.add(government)

        except:
            print "Vvedena nedopustimaja komanda"
            return

        print "Vlast' dobavlena!"

    def remove_government(self):
        try:
            government_id = int(raw_input('Vvedite nomer Vlasti dlja udalenija: '))
            if self._government_collection.remove(government_id):
                print "Vlast' %d uspeshno udalena!" % government_id
            else:
                print "Jelement ne udalen!"
        except:
            print "Oshibka udalenija vlasti!"
            return

    def save_to_file(self):
        try:
            self._government_collection.save_to_file()
        except:
            print "Oshibka zapisi v fajl"
            return
        print "Baza uspeshna sohranena"

    def create_from_file(self):
        try:
            self._government_collection = GovernmentCollection.create_from_file()
        except:
            print "Ne mogu sozdat' katalog iz fajla!"
            return
        print "Katalog uspeshno importirovan!"

    def close_program(self):
        import sys

        sys.exit()

    def handle_input(self, command):
        try:
            command = int(command)
            options = {
                0: self.close_program,
                1: self.print_catalog,
                2: self.add_government,
                3: self.remove_government,
                4: self.save_to_file,
                5: self.create_from_file,
            }
            options[command]()

        except TypeError:
            return
        except Exception as exs:
            print exs.message
            print "Vvedena nedopustimaja komanda"
            return

    def main(self):
        while True:
            self.print_hint()
            input_command = raw_input(">>>")
            self.handle_input(input_command)


InputHandler().main()