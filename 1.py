class ahmed:
    def __init__ (self,a,b):
        self.x=a
        self.y=b
    def distance(self,a):
        x=(self.x-a)**2
        y=(self.y-a)**2
        return (x+y)**0.5
f=ahmed(8,9)
print(f.x)
print(f.y)        
print(f.distance(3))
