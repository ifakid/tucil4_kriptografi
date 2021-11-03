import random
import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
              197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
              311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
              431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
              557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
              661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
              809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
              937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def generate_prime(bit_length):
    while True:
        num = random.getrandbits(bit_length)
        if num < 2 ** (bit_length / 2):
            continue
        if not low_test(num):
            continue
        if not miller_rabin(num):
            continue
        return num

def miller_rabin(num, loop=25):
    d = num-1  # Odd number
    r = 0  # Power of 2
    while d % 2 == 0:
        r += 1
        d >>= 1

    def witness(a):  # Composite witness
        if pow(a, d, num) == 1:
            return False
        for i in range(r):
            if pow(a, (2 ** i) * d, num) == (num - 1):
                return False  # Not composite
        return True

    for round in range(loop):  # Witness loop
        a = random.randrange(2, num - 1)
        if witness(a):
            return False
    return True


def low_test(num):
    for prime in primes:
        if not num % prime:  # Not prime
            return False
        elif prime**2 > num:  # No need to check the next ones
            return True
    return True


def toitent(p, q):
    return (p - 1) * (q - 1)


def is_coprime(a, b):
    return math.gcd(a, b) == 1


def lcm(x, y):
    return (x*y)//math.gcd(x,y)
