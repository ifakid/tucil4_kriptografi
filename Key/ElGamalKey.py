import random
from Util import prime
import json


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

    def export_public_key(self, path):
        if path.split('.')[-1] != 'pub':
            path += '.pub'
        pub_key = {
            'p': self.p,
            'g': self.g,
            'y': self.y
        }
        with open(path, 'w') as f:
            json.dump(pub_key, f)

    def import_public_key(self, path):
        if path.split('.')[-1] != 'pub':
            raise ValueError('Invalid file extension!')
        with open(path, 'r') as f:
            pub_key = json.load(f)
            self.p = pub_key['p']
            self.g = pub_key['g']
            self.y = pub_key['y']

    def import_private_key(self, path):
        if path.split('.')[-1] != 'pri':
            raise ValueError('Invalid file extension!')
        with open(path, 'r') as f:
            pri_key = json.load(f)
            self.p = pri_key['p']
            self.x = pri_key['x']

    def export_private_key(self, path):
        if path.split('.')[-1] != 'pri':
            path += '.pri'
        pri_key = {
            'p': self.p,
            'x': self.x
        }
        with open(path, 'w') as f:
            json.dump(pri_key, f)


if __name__ == '__main__':
    key = ElGamalKey()
    key.generate_key(128)
    key.export_private_key('eg128')
    key.export_public_key('eg128')