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

class Button:
    def __init__(self, text, type=('Кнопка'), loc=('')):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

    # экземпляр класса
text_box = Button('Text Box')
check_box = Button('Check Box')
radio = Button('Radio Button')
web = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_l = Button('Broken Links')
u_d = Button('Upload and Download')
    # вызываем метод
print(text_box.click())
print(check_box.click())
print(radio.click())
print(web.click())
print(buttons.click())
print(links.click())
print(broken_l.click())
print(u_d.click())
print('\n')

