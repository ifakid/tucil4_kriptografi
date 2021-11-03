import random
from Util import prime, other
import json


class RSAKey:
    def __init__(self):
        self.p = None
        self.q = None
        self.n = None
        self.e = None
        self.d = None
        self.phi = None

    def generate_key(self, key_length):
        while True:
            self.p = prime.generate_prime(key_length // 2)
            self.q = prime.generate_prime(key_length // 2)
            self.n = self.p * self.q
            if self.n.bit_length():
                break
        self.phi = prime.toitent(self.p, self.q)

        while True:
            self.e = random.randint(2, self.phi)
            if prime.is_coprime(self.e, self.phi):
                break

        self.d = pow(self.e, -1, self.phi)
        assert ((self.e * self.d) % self.phi == 1)

    def export_public_key(self, path):
        if path.split('.')[-1] != 'pub':
            path += '.pub'
        pub_key = {
            'n': self.n,
            'e': self.e
        }
        with open(path, 'w') as f:
            json.dump(pub_key, f)

    def import_public_key(self, path):
        if path.split('.')[-1] != 'pub':
            raise ValueError('Invalid file extension!')
        with open(path, 'r') as f:
            pub_key = json.load(f)
            self.n = pub_key['n']
            self.e = pub_key['e']

    def export_private_key(self, path):
        if path.split('.')[-1] != 'pri':
            path += '.pri'
        pri_key = {
            'p': self.p,
            'q': self.q,
            'n': self.n,
            'e': self.e,
            'd': self.d
        }
        with open(path, 'w') as f:
            json.dump(pri_key, f)

    def import_private_key(self, path):
        if path.split('.')[-1] != 'pri':
            raise ValueError('Invalid file extension!')
        with open(path, 'r') as f:
            pri_key = json.load(f)
            self.p = pri_key['p']
            self.q = pri_key['q']
            self.n = pri_key['n']
            self.e = pri_key['e']
            self.d = pri_key['d']


if __name__ == '__main__':
    key = RSAKey()
    key.generate_key(1024)
    hex_rep = format(key.n, 'x')
    print(hex_rep)
    print(int(hex_rep, 16))

