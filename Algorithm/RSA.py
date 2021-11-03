from Key import RSAKey
import math
import random
from Util import padding

class RSA:
    def __init__(self, key: RSAKey):
        self.key = key

    def generate_key(self, key_length):
        self.key.generate_key(key_length)

    def encrypt(self, m: bytes):
        if not self.key.e or not self.key.n:
            raise ValueError('Key invalid')
        if isinstance(m, str):
            m = m.encode()
        total_size = math.ceil(self.key.n.bit_length() / 8)
        chunk_size = total_size - 11  # total_size = 3 bytes flags + at least 8 bytes padding + message chunk
        plain_chunks = [m[i:i+chunk_size] for i in range(0, len(m), chunk_size)]
        encrypted_chunks = []

        def nonzero_byte():
            b = random.getrandbits(8)
            while b == 0x00:
                b = random.getrandbits(8)
            return b.to_bytes(1, byteorder='big')

        for chunk in plain_chunks:
            '''c_len = len(chunk)
            p_len = total_size - 3 - c_len
            padding = nonzero_byte() * p_len
            m_chunk = b'\x00\x02'+padding+b'\x00'+chunk  # PKCS#1 v1.5 padding'''
            m_chunk = padding.pkcs1_pad(chunk, total_size)
            encrypted_chunks.append(self._encrypt(m_chunk, total_size))
        encrypted = b''.join(encrypted_chunks)
        return encrypted

    def _encrypt(self, m: bytes, block_size):
        i = int.from_bytes(m, byteorder='big')
        return pow(i, self.key.e, self.key.n).to_bytes(block_size, byteorder='big')

    def decrypt(self, m: bytes):
        if not self.key.d or not self.key.n:
            raise ValueError('Key invalid')
        block_size = math.ceil(self.key.n.bit_length() / 8)
        encrypted_blocks = [m[i:i+block_size] for i in range(0, len(m), block_size)]
        decrypted_blocks = []
        for block in encrypted_blocks:
            decrypted_block = self._decrypt(block, block_size)
            decrypted_blocks.append(decrypted_block.split(b'\x00', 2)[-1])
        decrypted = b''.join(decrypted_blocks)
        return decrypted

    def _decrypt(self, m: bytes, block_size):
        i = int.from_bytes(m, byteorder='big')
        return pow(i, self.key.d, self.key.n).to_bytes(block_size, byteorder='big')


if __name__ == '__main__':
    key = RSAKey.RSAKey()
    key.generate_key(512)
    rsa = RSA(key)
    with open('../Example/cow.png', 'rb') as f:
        message = f.read()
        encrypted = rsa.encrypt(message)
        print("Encryption finished!")
        # print(encrypted)
        with open('encrypted.txt', 'wb') as w:
            w.write(encrypted)

    with open('encrypted.txt', 'rb') as f:
        file = f.read()
        decrypted = rsa.decrypt(encrypted)
        print("Decryption finished!")
        with open('decrypted.png', 'wb') as w:
            w.write(decrypted)
        # print(decrypted)
