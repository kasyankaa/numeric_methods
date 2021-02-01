import math
import numpy as np


def f(x):
    return (1 / (x * (math.sqrt(9 - x * x))))


def F(x):
    return (1 / 3) * np.log(x / (3 + (math.sqrt(9 - x * x))))


def left_rectangle(a, b, n=30):  # метод лівих прямокутників
    integral = 0
    h = (b - a) / n  # Обчислюємо величину кроку h
    x = a

    for i in range(0, n - 1):  # квадратна сума
        integral += f(x)
        x += h
    integral *= h
    return integral


def newton_leibniz(a, b):
    return F(b) - F(a)


def main():
    a = float(input('enter a: '))
    b = float(input('enter b: '))

    print('left rectangle: ' + str(left_rectangle(a, b)))
    print('newton-leibniz formula: ' + str(newton_leibniz(a, b)))  # перевірка


if __name__ == '__main__':
    main( )
