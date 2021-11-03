import random
from Util import prime
import math


class PaillierKey:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.phi = 0
        self.lam = 0
        self.g = 0
        self.mu = 0

    def generate_key(self, key_length):
        while True:
            self.p = prime.generate_prime(key_length // 2)
            self.q = prime.generate_prime(key_length // 2)
            self.n = self.p * self.q
            self.phi = prime.toitent(self.p, self.q)
            if prime.is_coprime(self.n, self.phi):
                break
        self.lam = math.lcm(self.p - 1, self.q - 1)
        self.g = random.randrange(self.n ** 2)

        self.mu = pow(self.L(pow(self.g, self.lam, self.n ** 2)), -1, self.n)

    def L(self, x):
        return (x - 1) / self.n

    def import_key(self, path):
        pass

    def export_key(self, path):
        pass
