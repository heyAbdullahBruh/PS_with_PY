# Problem -39 --- Time Class --> 
# Attributes: hours, minutes
# Method: add_time(t2) → returns total time


from math import floor

class Time :
    def __init__(self,hours, minutes):
          self.hours=hours
          self.minutes=minutes
    def add_time(self, hours, minutes):
        minutesSum = self.minutes + minutes
        hoursSum = self.hours + hours

        if minutesSum >= 60 :
            self.hours = hoursSum + floor(minutesSum/60)
            self.minutes = floor(minutesSum%60)
            return
        self.hours = hoursSum 
        self.minutes = minutesSum
        
    def display(self) :
        return f"Running time is {self.hours} : {self.minutes:02d} "

time1= Time(4,30)    
print(time1.display())

time1.add_time(4,31)
print(time1.display())

