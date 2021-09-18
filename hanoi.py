import time
import os


def one_step(X, Y):
    for i in range(1, level + 1):
        if Y[len(Y) - i] == '':
            for j in range(0, level):
                if X[j] != '':
                    Y[len(Y) - i] = X[j]
                    X[j] = ''
                    break
            break


def move(N, first, third, second):
    if N == 1:
        one_step(first, third)
        paint(level, A, B, C)

    elif N > 1:
        move(N-1, first, second, third)
        one_step(first, third)
        paint(level, A, B, C)
        move(N-1, second, third, first)


def paint(lev, list1, list2, list3):
    os.system("cls")
    print("\n")
    for i in range(0, lev):
        print('{0:>{width}}   {1:^{width}}   {2:<{width}}'.format(list1[i], list2[i], list3[i], width=str(level)))
    print('-' * level + "   " + '-' * level + "   " + '-' * level)
    time.sleep(counter)


while True:
    co_robimy = input("Jesli chcesz zagrac w wieze wybierz 'y', jesli chcesz zakonczyc wybierz 'n': ")

    if co_robimy == 'y':
        level = int(input("ilosc kolumn w Wieży Hanoi: "))
        counter = float(input("Co ile sekund ma sie pojawic nowe ustawienie? "))
        A = ['X' * i for i in range(1, level + 1)]
        B = [''] * level
        C = [''] * level

        os.system("cls")
        paint(level, A, B, C)
        move(level, A, C, B)
        input('Press ENTER to exit')
        os.system("cls")

    elif co_robimy == 'n':
        break



input('Press ENTER to exit')