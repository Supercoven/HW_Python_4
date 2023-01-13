#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
#  элементов исходной последовательности в том же порядке.

import random

def randomlist():
    r_list = []
    for i in range (10): # magic number, просто чтобы список был небольшой
        num = random.randint(1,10) # до 10 чтобы больше шанс повтора
        r_list.append(num)
    return r_list

new_list = randomlist()
print(f'Первоначальный список: {new_list}')

def clear_list(create_list):

    remove_num = list(set(create_list))
    print(f'Список после очистки от повторяющихся элементов: {remove_num}')

create_list = randomlist()
clear_list(create_list)