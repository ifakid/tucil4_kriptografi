from Key.PaillierKey import PaillierKey
import random
from Util.prime import is_coprime


class Paillier:
    def __init__(self, key: PaillierKey):
        self.key = key

    def encrypt(self, m:bytes):
        if not (self.key.g and self.key.n):
            raise ValueError('Key invalid!')
        block_length = self.key.n.bit_length() - 1
        plain_blocks = [m[i:i + block_length] for i in range(0, len(m), block_length)]
        encrypted_blocks = []
        for block in plain_blocks:
            encrypted_blocks.append(self._encrypt(block, block_length))
        return b''.join(encrypted_blocks)

    def _encrypt(self, m: bytes, block_length):
        while True:
            r = random.randrange(0, self.key.n)
            if is_coprime(r, self.key.n):
                break
        i = int.from_bytes(m, byteorder='big')
        c = (pow(self.key.g, i, self.key.n**2)*pow(r, self.key.n, self.key.n**2)) % (self.key.n**2)
        return c.to_bytes(block_length, byteorder='big')

    def decrypt(self, m: bytes):
        if not (self.key.lam and self.key.mu):
            raise ValueError('Key invalid!')
        block_length = self.key.n.bit_length() - 1
        encrypted_blocks = [m[i:i + block_length] for i in range(0, len(m), block_length)]
        decrypted_blocks = []
        for block in encrypted_blocks:
            decrypted_blocks.append(self._decrypt(block, block_length))
        return b''.join(decrypted_blocks)

    def _decrypt(self, m: bytes, block_length):
        i = int.from_bytes(m, byteorder='big')
        lc = self.key.L(pow(i, self.key.lam, self.key.n ** 2))
        p = (lc * self.key.mu) % self.key.n
        return p.to_bytes(block_length, byteorder='big')


if __name__ == '__main__':
    g = 5652
    i = 42
    r = 23
    n = 77
    print((pow(g, i) * pow(r, n)) % (n ** 2))
    print((pow(g, i, n ** 2) * pow(r, n, n ** 2)) % (n ** 2))