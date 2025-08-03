# Problem -35 Make a Area calculator with Python Classes --> 
# Scpecially --> circle , Tringle , Traphiziam --->

from abc import ABC, abstractmethod

class Item(ABC) :
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @abstractmethod
    def calc(self) : 
        pass


class Circle(Item) : 
    def __init__(self,a,b):
        super().__init__(a,b)
    def calc(self):
        return f"This circle Area is = {self.a*self.b**2}"
    def circumference(self):
        return f"This circle circumference is = {2*self.a*self.b}"

circle1= Circle(3.1618,5)
print(circle1.calc()) #This circle Area is = 79.045
print(circle1.circumference())#This circle circumference is = 31.618



class Tringle (Item):
    def __init__(self,a,b):
        super().__init__(a,b)
    def calc(self):
    # a= base , b= height
        return f"This Tringle Area is = {self.a*self.b*.5}"
    def perimeter (self):
    # a= base , b=  sides
        return f"This Tringle perimeter  is = {2*self.a+self.b}"
tringle1= Tringle(3.1618,5)
print(tringle1.calc()) #This Tringle Area is = 7.9045
print(tringle1.perimeter())#This Tringle perimeter  is = 11.323599999999999


class Traphiziam(Item):
     def __init__(self,a,b,c,d,h):
        super().__init__(a,b)
        self.c=c
        self.d=d
        self.h=h
     def calc(self):
         return f"This Traphiziam Area is = {.5*(self.a+self.b)*self.h}"
     def perimeter (self):
        return f"This Tringle perimeter  is = {self.a+self.b+self.c+self.d}"

trapezium1= Traphiziam(4,7,5,8,4)
print(trapezium1.calc()) # This Traphiziam Area is = 22.0
print(trapezium1.perimeter())# This Tringle perimeter  is = 24

