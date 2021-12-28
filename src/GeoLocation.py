import math

import api
from api import GeoLocation

class GeoLocationClass(api.GraphInterface):


    #constructor
    def __init__(self, location):
        #instance fields found by Java to Python Converter:
        location = None
        self.__s = []
        self.__x = 0
        self.__y = 0
        self.__z = 0

        self.__location = location
        self.__s = location.split(",")
        self.__x = float(self.__s[0])
        self.__y = float(self.__s[1])
        self.__z = float(self.__s[2])

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z

    def distance(self, g):
        return math.sqrt(self.__x - g.x() ** 2 + self.__y - g.y() ** 2 + self.__z - g.z() ** 2)
    def toString(self):
        return self.__location
