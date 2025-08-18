#Problem-9.1 Rectangle class --> 

class Rectangle : 
    def __init__(self,width=float,length=float):
        self.width=width
        self.length=length
    def area(self):
        return f"This Rectangle's Area is = {self.width *self.length} "
    
    def is_square(self):
        if self.width ==self.length :
            return "It's a square"
        return "It isn't a square"