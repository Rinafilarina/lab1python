import time 
import sys
import os
import math

BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
RED = '\u001b[41m'
BLACK = '\u001b[40m'
YELLOW = '\u001b[43m'
RESET = '\u001b[0m'

def flag(): #флаг Франции (вариант 1)
    height = 10
    length = 12
    pixel = '   '
    for i in range(height):
        print(BLUE + pixel*(length//3) + WHITE + pixel*(length//3) + RED + pixel*(length//3) + RESET)

def drawing(): #рисунок а
    if len(sys.argv)>1: 
        length = int(sys.argv[1])
    else:
        length = 5
    for i in range(length):
        pixel = ' '
        for h in range(3):
            print(BLACK + pixel + WHITE + pixel + BLACK + pixel + RESET)
            print(WHITE + pixel + BLACK + pixel + WHITE + pixel + RESET)

def history(): #анимация(убрать #, чтобы посмотреть)
    year = 1900
    height = 12
    length = 16
    pixel = '   '
    for i in range(height//3):
        print(BLACK + pixel*length + RESET)
    for i in range(height//3):
        print(YELLOW + pixel*length + RESET)
    for i in range(height//3):
        print(WHITE + pixel*length + RESET)
    while year<=1922:
        print(f'\u001b[20D{year}', end='', flush=True)
        time.sleep(0.1)
        year+=1
    os.system('cls')
    height = 12
    length = 16
    pixel = '   '
    print(RED + pixel*length + RESET)
    print(RED + pixel + YELLOW + pixel + RED + pixel*(length-2) + RESET)
    for i in range(height-2):
        print(RED + pixel*length + RESET)
    while year<=1991:
        print(f'\u001b[20D{year}', end='', flush=True)
        time.sleep(0.1)
        year+=1
    os.system('cls')
    height = 12
    length = 16
    pixel = '   '
    for i in range(height//3):
        print(WHITE + pixel*length + RESET)
    for i in range(height//3):
        print(BLUE + pixel*length + RESET)
    for i in range(height//3):
        print(RED + pixel*length + RESET)
    while year <=2000:
        print(f'\u001b[20D{year}', end='', flush=True)
        time.sleep(0.1)
        year+=1

def sequence(): #диаграмма - количество чисел больше и меньше 0
    file = open('sequence.txt', 'r')
    mzero = 0
    bzero = 0
    for line in file:
        if float(line)<0:
            mzero+=1
        else:
            bzero+=1
    file.close()
    print(f'{BLUE}{" "*int(mzero/5)}{RESET}{mzero*100/(mzero+bzero)}%')
    print(f'{RED}{" "*int(bzero/5)}{RESET}{bzero*100/(mzero+bzero)}%')

def func(): #доп. задание - y=x^2
    print('y=x^2')
    height = 90
    length = 35
    pixel = ' '
    for y in range(height, -1, -1):
        xnow = round(math.sqrt(y/10), 1)
        print(f'{WHITE}{pixel*(int(xnow*10))}{BLACK}{pixel}{WHITE}{pixel*(length - 1 - int(xnow*10))}{RESET}')
    for i in range(0, 4):
        print(str(i) + pixel*9, end='')


flag()
drawing()
#history()
sequence()
func()