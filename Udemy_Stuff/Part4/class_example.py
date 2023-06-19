class Point():
    """ Point class for representing and manipulating x,y coordinates"""
    count_of_point = 0 # this is a class variable
    def __init__(self, initX, initY):
        """ this is an initializer method, often referred to ask the constructor"""
        self.x = initX
        self.y = initY

    def get_x(self) -> any:
        return self.x

    def get_y(self):
        return self.y

    def __str__(self) -> str: # Print out an instance as a string
        return 'x-axis: {} , y-axis : {}'.format(self.x, self.y)

    def __add__(self, other_point):  # overloading + operator for the class
        return Point(self.x + other_point.x, self.y + other_point.y)

    # overloading the - operator for the class
    def __substraction__(self, otherPoint):
        return Point(self.x - otherPoint.x, self.y - otherPoint.y)
    
    def halfway(self, target):
        mx = (self.x + target) / 2
        my = (self.y + target) / 2
        return Point(mx, my)
    
    def sort_priority(self): # used for the sorted function as the key to sort by
        return self.x


q = Point(1, 2)
x = Point(2, 3)
print(q.get_x())
print(q+x)
lst = [Point(1,2), Point(4,3), Point(2,4)]

print(sorted(lst, key = Point.sort_priority))
