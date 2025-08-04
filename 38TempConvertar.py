# Problem->38, Make a temparature converter by Python class -->

from enum import Enum

class TempType (Enum):
    cl ='cl'
    fh ='fh'
    kl ='kl'

class TempConverter :
    def __init__(self,tempQuant=float, tempType=TempType):
        self.tempQuant=tempQuant
        self.tempType=tempType

    def to_fahrenheit(self):
        if(self.tempType=='fh'):
            return f"The temparature is Now {self.tempQuant} deg fh."
        elif(self.tempType=='cl'):
            convert= (self.tempQuant *(9/5)) + 32
            return f"Celsius temparature is Fahrenheit on = {convert} deg fh."
        elif(self.tempType=='kl'):
            convert= ((self.tempQuant - 273.15) * (9/5) )+ 32
            return f"Kelvin temparature is Fahrenheit on = {convert} deg fh."
        
    def to_celsius(self):
        if(self.tempType=='cl'):
            return f"The temparature is Now {self.tempQuant} deg cl."
        elif(self.tempType=='fh'):
            convert= (self.tempQuant -32) * (5/9) 
            return f"Fahrenheit temparature is Celsius on = {convert} deg cl."
        elif(self.tempType=='kl'):
            convert= self.tempQuant - 273.15
            return f"Kelvin temparature is Celsius on = {convert} deg cl."
        
    def to_kelvin(self):
        if(self.tempType=='kl'):
            return f"The temparature is Now {self.tempQuant} deg kl."
        elif(self.tempType=='fh'):
            convert= ((self.tempQuant -32) * (5/9) )+273.15
            return f"Fahrenheit temparature is Kelvin on = {convert} deg kl."
        elif(self.tempType=='cl'):
            convert= self.tempQuant + 273.15
            return f"Celsius temparature is Kelvin on = {convert} deg kl."

# Celcius-->
celcius = TempConverter(33.3,'cl')
print(celcius.to_celsius()) # The temparature is Now 33.3 deg cl.
print(celcius.to_fahrenheit())# Celsius temparature is Fahrenheit on = 91.94 deg fh.
print(celcius.to_kelvin()) # Celsius temparature is Kelvin on = 306.45 deg kl.

# Farenheit-->
farenheit = TempConverter(105,'fh')
print(farenheit.to_celsius()) # Fahrenheit temparature is Celsius on = 40.55555555555556 deg cl.
print(farenheit.to_fahrenheit())# The temparature is Now 105 deg fh.
print(farenheit.to_kelvin()) # Fahrenheit temparature is Kelvin on = 313.7055555555555 deg kl.

# Kelvin-->
kelvin = TempConverter(310,'kl')
print(kelvin.to_celsius()) # Kelvin temparature is Celsius on = 36.85000000000002 deg cl.
print(kelvin.to_fahrenheit())# Kelvin temparature is Fahrenheit on = 98.33000000000004 deg fh.
print(kelvin.to_kelvin()) # The temparature is Now 310 deg kl.

