# -*- coding: utf8 -*-
__author__ = 'kholodnyak'

from geom.shape import Point
from geom.shape import Shape


class Vector(Shape):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iadd__(self, other):
        self.end.x += other.end.x - other.start.x
        self.end.y += other.end.x - other.start.y

    def __isub__(self, other):
        self.end.x = self.end.x - other.end.x + other.start.x
        self.end.y = self.end.y - other.end.y + other.start.y

    def __len__(self):
        return Point.len_to(self.end - self.start)

    def __lt__(self, other):
        return len(self) < len(other)




