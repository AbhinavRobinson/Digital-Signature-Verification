"""
    ! Set of Functions to Generate Keys

    Generates private and public key pair

    p_num1 = first prime
    p_num2 = second prime
    key_size = define key size (128 bits : default)
"""

# Imports random for randomint generation 
import random

def generate(p_num1, p_num2, key_size=128):

    n = p_num1 * p_num2
    tot = (p_num1 - 1) * (p_num2 - 1)

    e = generatePublicKey(tot, key_size)
    d = generatePrivateKey(e, tot)

    return e, d, n

# Generates public key
def generatePublicKey(tot, key_size):

    e = random.randint(2**(key_size-1), 2**key_size - 1)
    g = gcd(e, tot)

    while g != 1:

        e = random.randint(2**(key_size-1), 2**key_size - 1)
        g = gcd(e, tot)

    return e

# Generates private key
def generatePrivateKey(e, tot):

    d = egcd(e, tot)[1]
    d = d % tot

    if d < 0:
        d += tot

    return d

# Euclidian GCD
def egcd(a, b):

    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)

    return (g, x - (b // a) * y, y)

# Greatest Comman Divisor
def gcd(e, tot):

    temp = 0

    while True:

        temp = e % tot

        if temp == 0:
            return tot

        e = tot
        tot = temp

# Check if num is prime
def isPrime(num):

    if num < 2:
        return False
    if num == 2:
        return True
    if num & 0x01 == 0:
        return False

    n = int(num ** 0.5)

    for i in range(3, n, 2):
        if num % i == 0:
            return False

    return True

# End Of generate_keys.py