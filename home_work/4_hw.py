class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        print(self.width * self.height)

    def perimeter(self):
        print(self.width + self.height)

r1 = Rectangle(10, 5)
r2 = Rectangle(8, 12)
r3 = Rectangle(7, 10)

r1.square()
r1.perimeter()
r2.square()
r2.perimeter()
r3.perimeter()
r3.square()
print('\n')
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)

m = Math(6, 3)
m.division()
m.subtraction()
m.addition()
m.multiplication()
print('\n')

