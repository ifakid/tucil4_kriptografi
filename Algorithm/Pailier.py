from Key.PaillierKey import PaillierKey
import random
from Util.prime import is_coprime
from Util import padding
import math


class Paillier:
    def __init__(self, key: PaillierKey, min_pad=8):
        self.key = key
        self.pad = min_pad

    def encrypt(self, m: bytes):
        if not (self.key.g and self.key.n):
            raise ValueError('Key invalid!')
        total_length = math.ceil(self.key.n.bit_length()/8)
        block_length = total_length - 3 - self.pad
        if block_length <= 0:
            raise ValueError("Key is too short!")
        plain_blocks = [m[i:i + block_length] for i in range(0, len(m), block_length)]
        encrypted_blocks = []
        for block in plain_blocks:
            padded = padding.pkcs1_pad(block, total_length)
            encrypted_blocks.append(self._encrypt(padded, total_length))
        return b''.join(encrypted_blocks)

    def _encrypt(self, m: bytes, block_length):
        while True:
            r = random.randrange(0, self.key.n)
            if is_coprime(r, self.key.n):
                break
        m_byte = int.from_bytes(m, byteorder='big')
        c = (pow(self.key.g, m_byte, self.key.n**2) * pow(r, self.key.n, self.key.n**2)) % (self.key.n**2)
        return c.to_bytes(block_length*2, byteorder='big')

    def decrypt(self, m: bytes):
        if not (self.key.lam and self.key.mu and self.key.n):
            raise ValueError('Key invalid!')
        block_length = math.ceil(self.key.n.bit_length()/8)
        print(f'block_length {block_length}')
        encrypted_blocks = [m[i:i + block_length*2] for i in range(0, len(m), block_length*2)]
        decrypted_blocks = []
        for block in encrypted_blocks:
            p_text = self._decrypt(block, block_length)
            decrypted_blocks.append(padding.pkcs1_unpad(p_text))
        return b''.join(decrypted_blocks)

    def _decrypt(self, m: bytes, block_length):
        c = int.from_bytes(m, byteorder='big')
        lc = self.key.L(pow(c, self.key.lam, self.key.n ** 2))
        p = (lc * self.key.mu) % self.key.n
        return p.to_bytes(block_length, byteorder='big')


if __name__ == '__main__':
    key = PaillierKey()
    key.generate_key(128)

    with open('../Example/text.txt', 'rb') as f:
        message = f.read()

        p = Paillier(key)
        enc = p.encrypt(message)
        print(enc)

        dec = p.decrypt(enc)
        print(dec)
