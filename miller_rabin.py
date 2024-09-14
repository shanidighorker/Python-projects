"""
student:shani dihorker
Assigment no.2
program:miller_rabin
"""
import random
def get_even_odd_parts(n): #section1
    """
    A function that accepts a positive integer n
    and returns a pair of numbers: (n(even) and (n(odd
    """
    degree = 0
    odd = 0
    even = 0
    while (2**degree) <= n:
        if n % (2**degree) == 0:
            even = degree
        degree += 1
    odd = n//(2**even)
    return even, odd

def is_probably_prime(n): #section 2
    s, t = get_even_odd_parts(n-1)
    for _ in range(10):
        if not is_suspected_prime(n, t, s) == False:  # step 2+3
            return False
    return True


def power_modular(x, b, n):
    """
    Calculates x**e mod n"""
    result = 1
    x = x % n
    while b > 0:
        if b % 2 == 1:
            result = (result * x) % n
        b = b // 2
        x = (x * x) % n
    return result

def is_suspected_prime(n:int, t:int, s:int)->bool: #section3
    a = random.randint(2, n-1)  # choose a random positive integer a between 2 and n-1 -- #sec1

    d = power_modular(a, t, n) #sec2

    if d == 1 or d == n - 1: #sec3
        return True

    for i in range(1, s):  #for i = 1 to s – 1 -- #sec4
        d = power_modular(d, 2, n) #d = d**2 mod n
        if d == n - 1:
            return True
    return False

def number_odd_random_make(m:int) -> int: #section4
    """
    A function that accepts an integer as a parameter
    positive m and returns an odd random number
    """
    number = 0
    for i in range(m):
        digit = random.randint(1, 9)
        if digit % 2 == 0: #For testing whether the chosen random number is even
            digit += 1  #If the chosen number is really odd we will subtract 1 from it to make it odd
        number = number * 10 + digit #Saves the number after selecting it by multiplying the current number
        # by 10 and adding the random number
    return number

def make_prime(m:int)->int: #section5
    """A function that accepts a positive integer parameter m and returns
    A prime number of length m decimal digits.
    """
    while True:
        n = (number_odd_random_make(m))
        if is_probably_prime(m):
            return n
def main():
    even, odd = get_even_odd_parts(12)
    print(even)
    print(odd)
    print(is_probably_prime(20))
    print(number_odd_random_make(50))
    print('hellow')

main()





