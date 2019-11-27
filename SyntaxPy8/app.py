class Point:

    def __init__(self,x,y):#CONSTRUCTOR, init is short for initialize
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

# point1 = Point()#instance/object of a class
# point1.move()
# point1.draw()
# point1.x = 10
# point1.y = 20
# print(point1.x)
#
# point2 = Point()
# point2.x = 1
# print(point2.x)

point = Point(10,20)
print(point.x,point.y)