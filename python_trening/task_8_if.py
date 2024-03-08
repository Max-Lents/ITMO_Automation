# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение

# num = 3

# num = -5
num = 0

if num >= 0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('да')
    else:
        print('нет')
task_yes_no(str_1 = 'test', str_2 = 'test1')

num_float = 3.4

if num_float > 0:
    print('положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def student_rank(year_of_study):
    if year_of_study in range(1, 5):
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистрант')
    elif year_of_study in range(7, 10):
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(4)

a = 13

if a > 100 or a < -100:
    print('-')
else:
    print('+')