# Problem-33 ---> Car speed controller ---->
# accelerate(), brake(), status()
class Car : 
    def __init__(self,brand,max_speed):
        self.brand=brand
        self.max_speed=max_speed
        self.speed=0
    def accelerate(self):
        self.speed+=20
        if self.speed > self.max_speed :
            self.speed =self.max_speed
            return
    def brake(self):
        self.speed-=20
        if self.speed <= 0 :
            self.speed =0
            return
    def status(self):
        return f"{self.brand} is running at {self.speed} km/h "
tesla = Car('Tesla',150)
print(tesla.status()) #Tesla is running at 0 km/h    
tesla.accelerate()
print(tesla.status()) #Tesla is running at 20 km/h    
tesla.accelerate()
tesla.accelerate()
tesla.accelerate()
print(tesla.status()) #Tesla is running at 80 km/h    

tesla.brake()
print(tesla.status()) #Tesla is running at 60 km/h    
