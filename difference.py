"""
student:shani dihorker
Assigment no.1
program:difference
"""
import random
from math import sin


def difference(f, g): #section1
    return lambda x: f(x)-g(x)

def diff(f):
    ''' returns the numeric derivative of f '''
    #פונקצייה שמחשבת את הנגזרת
    h = 0.000001
    return (lambda x: (f(x+h)-f(x))/h)

def nr(f, a, b, epsilon, n):
    counter = 0
    while (True):
        x = random.randint(a, b)
        if diff(f)(x) < epsilon:
            continue
        else:
            break

    while(True):
        x = x-(f(x)/diff(f)(x))
        counter += 1
        if abs(f(x)) < epsilon:
            return x
        if counter >= n:
            return None

def main():
    f = lambda x: x**2 + 1
    g = lambda x: x**3 - 2
    # print(difference(f, g)(2))
    print(nr(lambda x: sin(x), 6, 8, 0.0000000001, 100))

main()
