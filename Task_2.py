#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def create_list(numList):
    numList = int(numList)
    numArr = [i for i in range(1, numList + 1)]
    arrPrime = []
    for j in numArr:
        if j > 1:
            for n in range(2, j):
                if(j%n) == 0:
                    break
            else:
                arrPrime.append(j)
    return arrPrime

def addListPrime(numMulti, num):
    num = int(num)
    print(f'На входе список из простых чисел {numMulti}, тип: {type( numMulti[0] )}\n'
          f'Интервал списка: от 1 до {num}, тип: {type(num)}')

    arrListPrime = []
    for i in numMulti:

        while(num % i == 0):
            num = num / i
            print(f'num={num} , i ={i}')
            arrListPrime.append(i)
        else:
            continue

    print(f'Простые множители числа {num}: {arrListPrime}')


num = input('Введите число для составления списка простых множителей:')

numMulti = create_list(num)
addListPrime(numMulti, num)
