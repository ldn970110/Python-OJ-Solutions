class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
         print(self.x,self.y)
    def distance(self,tx,ty):
        return (((self.x-tx)**2)+(self.y-ty)**2)**0.5
p=Point(97887,9)
p.show()
r=p.distance(0,0)
print(r)