# Problem --> 40 - Point class -->
# Represents a 2D coordinate point (like on a graph) and can find the distance to another point.
# Key Formula --> sqrt((x1-x2)**2 +(y1+y2)**2 )

from math import sqrt

class Graph :
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def pointCalc (self):
        x1=self.x1
        x2=self.x2
        y1=self.y1
        y2=self.y2
        
        result = sqrt((x1-x2)**2+(y1-y2)**2)
        return result

graph1 = Graph(1,2,1,1)

print(graph1.pointCalc()) # 1

 