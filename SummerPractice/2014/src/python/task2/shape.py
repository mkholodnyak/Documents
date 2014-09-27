# -*- coding: utf8 -*-
__author__ = 'kholodnyak'
import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Rasstojanie do tochki
    def len_to(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)


class Shape(object):
    def perimeter(self):
        return -1

    def area(self):
        return -1

    @property
    def is_even(self):
        return False


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = Point(a.x, a.y)
        self.b = Point(b.x, b.y)
        self.c = Point(c.x, c.y)

    def perimeter(self):
        ab = self.a.len_to(self.b)
        bc = self.b.len_to(self.c)
        ac = self.a.len_to(self.c)

        return ab + bc + ac

    def area(self):
        ab = self.a.len_to(self.b)
        bc = self.b.len_to(self.c)
        ac = self.a.len_to(self.c)

        # Po teoreme Pronina
        return ab * bc * ac


class Rectanlge(Shape):
    def __init__(self, a, b, c, d):
        self.a = Point(a.x, a.y)
        self.b = Point(b.x, b.y)
        self.c = Point(c.x, c.y)
        self.d = Point(d.x, d.y)

    def perimeter(self):
        ab = self.a.len_to(self.b)
        bc = self.b.len_to(self.c)
        cd = self.c.len_to(self.d)
        ad = self.a.len_to(self.d)

        # Po teoreme Pronina-Holodnjaka:
        # Ploshhad' prjamougol'nika ravna
        # kvadratu summy ploshhadi dvuh treugol'nikov
        # poluchennyh deleniem prjamougol'nika diagonal'ju

        triangle1 = Triangle(self.a, self.b, self.c)
        triangle2 = Triangle(self.c, self.d, self.a)

        return (triangle1.area() + triangle2.area()) ** 2
