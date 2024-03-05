def task(a: int, b: float, c: str, d: list, e: bool) -> [int, float, str, list, bool]:
    return a, b, c, d, e
a = 1
print (a, "относится к типу ", type(a))
b = 1.0001
print(b, "относится к типу ", type(b))
c = 'строка'
print(c, "относится к типу ", type(c))
d = [1, 2, 3]
print(d, "относится к типу ", type(d))
e = True
if e:
    print('e == True')
else:
    print('e not True')

print(task(a, b, c, d, e))
print('\n')

def task_2(a: list) -> list:
    return 'a[0:3]', a[0:3]
a = [1, 2, 3, 5, 8, 13, 21]
print('a[0:3]', a[0:3])
print(task_2(a))
#упорядоченная последовательность
print('\n')


def task_3(a, b):
    return a ** b

print( task_3( 2, 4 ) )