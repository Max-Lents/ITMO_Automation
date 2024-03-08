def bigger_number(a, b):
    if a > b:
        print('Наибольшее число', a)
    elif b > a:
        print('Наибольшее число', b)
    else:
        print('Числа равны')
bigger_number(a = 5, b = 7)

def numbers_135(a, b):
    if a - b == 135 or b - a == 135:
        print('Yes')
    else:
        print('No')
numbers_135(a = 1, b = 136)

def year_season(num):
    if num in range(1, 4):
        print('Весна')
    elif num in range(4, 7):
        print('Лето')
    elif num in range(7, 10):
        print('Осень')
    elif num in range(10, 13):
        print('Зима')
year_season(12)

def number_bigger_10(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('no')
number_bigger_10(a = 11, b = 10, c = 12)

def positive_numbers(a):
    if a[0] > 0 and a[1] > 0 and a[2] > 0 and a[3] > 0 and a[4] > 0 and a[5] > 0:
        print(len(a[0:6]))
a = [-1, 0, 1, 2, 3]

positive_numbers(a)

def days(a, b):
 if a * 365 and b * 29:
     print(a * 365 + b * 29)
days(1, 1)