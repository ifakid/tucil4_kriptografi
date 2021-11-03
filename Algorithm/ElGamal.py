from Key.ElGamalKey import ElGamalKey
import random
from Util import padding
import math


class ElGamal:
    def __init__(self, key: ElGamalKey, min_pad=8):
        self.key = key
        self.pad = min_pad

    def encrypt(self, m: bytes):
        if not (self.key.p and self.key.g and self.key.y):
            raise ValueError('Key invalid!')
        total_length = math.ceil((self.key.p - 1).bit_length() / 8)  # Interval [0, p-1]
        block_length = total_length - 3 - self.pad
        if block_length <= 0:
            raise ValueError()
        plain_blocks = [m[i:i + block_length] for i in range(0, len(m), block_length)]
        encrypted_blocks = []
        for i, block in enumerate(plain_blocks):
            # print(f'Encrypting {i+1}/{len(plain_blocks)}')
            padded = padding.pkcs1_pad(block, total_length)
            encrypted_blocks.append(self._encrypt(padded, total_length))
        return b''.join(encrypted_blocks)

    def _encrypt(self, m: bytes, block_length):
        k = random.randint(1, self.key.p - 2)
        i = int.from_bytes(m, byteorder='big')
        a = (pow(self.key.g, k, self.key.p)).to_bytes(block_length, byteorder='big')
        b = ((i * pow(self.key.y, k, self.key.p)) % self.key.p).to_bytes(block_length, byteorder='big')
        return a + b

    def decrypt(self, m: bytes):
        if not (self.key.p and self.key.x):
            raise ValueError('Key invalid!')
        block_length = math.ceil((self.key.p - 1).bit_length() / 8)  # Interval [0, p-1]
        encrypted_blocks = [m[i:i + block_length * 2] for i in range(0, len(m), block_length * 2)]
        decrypted_blocks = []
        for i, block in enumerate(encrypted_blocks):
            decrypted_blocks.append(self._decrypt(block))
        return b''.join(decrypted_blocks)

    def _decrypt(self, m: bytes):
        block_length = len(m) // 2
        a = int.from_bytes(m[:block_length], byteorder='big')
        b = int.from_bytes(m[block_length:], byteorder='big')
        a_inv = pow(a, self.key.p - 1 - self.key.x, self.key.p)
        decrypted = ((b * a_inv) % self.key.p).to_bytes(block_length, byteorder='big')
        return padding.pkcs1_unpad(decrypted)


if __name__ == '__main__':
    message = b'halooo'
    key = ElGamalKey()
    key.generate_key(128)
    eg = ElGamal(key)
    enc = eg.encrypt(message)
    print(enc)

    dec = eg.decrypt(enc)
    print(dec)
