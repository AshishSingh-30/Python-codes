class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*self.radius*3.14

r=float(input('Enter the radius of the circle : '))
c=Circle(r)
print('area of circle is : ',c.area(),' units')
print('perimeter is : ',c.perimeter(),' units')