import random
from Util import prime
import json


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
        self.lam = prime.lcm(self.p - 1, self.q - 1)

        while True:
            while True:
                self.g = random.randint(2, self.n ** 2)
                if prime.is_coprime(self.g, self.n**2):
                    break
            try:
                lpow = int(self.L(pow(self.g, self.lam, self.n ** 2)))
                self.mu = pow(lpow, -1, self.n)  # will return an error if L results in float
                break
            except:
                pass

    def L(self, x):
        return (x - 1) // self.n

    def export_public_key(self, path):
        if path.split('.')[-1] != 'pub':
            path += '.pub'
        pub_key = {
            'n': self.n,
            'g': self.g
        }
        with open(path, 'w') as f:
            json.dump(pub_key, f)

    def import_public_key(self, path):
        if path.split('.')[-1] != 'pub':
            raise ValueError('Invalid file extension!')
        with open(path, 'r') as f:
            pub_key = json.load(f)
            self.n = pub_key['n']
            self.g = pub_key['g']

    def export_private_key(self, path):
        if path.split('.')[-1] != 'pri':
            path += '.pri'
        pri_key = {
            'lam': self.lam,
            'mu': self.mu,
            'n': self.n
        }
        with open(path, 'w') as f:
            json.dump(pri_key, f)

    def import_private_key(self, path):
        if path.split('.')[-1] != 'pri':
            raise ValueError('Invalid file extension!')
        with open(path, 'r') as f:
            pri_key = json.load(f)
            self.lam = pri_key['lam']
            self.mu = pri_key['mu']
            self.n = pri_key['n']


if __name__ == '__main__':
    key = PaillierKey()
    key.generate_key(128)
    key.export_public_key('p128')
    key.export_private_key('p128')