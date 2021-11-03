import random
from Util import prime


class ElGamalKey:
    def __init__(self):
        self.p = 0
        self.g = 0
        self.x = 0
        self.y = 0

    def generate_key(self, bit_length):
        self.p = prime.generate_prime(bit_length)
        while self.p.bit_length() != bit_length:
            self.p = prime.generate_prime(bit_length)

        self.x = random.randint(1, self.p-2)
        self.g = random.randrange(self.p)
        self.y = pow(self.g, self.x, self.p)

    def import_key(self, path):
        pass

    def export_key(self, path):
        pass

