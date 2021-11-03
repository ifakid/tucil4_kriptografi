from Key.ECurve import *
from Key.ECKey import *
import math


class ECC:
    def __init__(self, key: ECKey):
        self.key = key

    def encrypt(self, m: bytes):
        if not (self.key and self.key.ec and self.key.base and self.key.k and self.key.pub):
            raise ValueError()
        block_length = math.ceil(self.key.ec.p.bit_length()/8)
        encrypted = b''
        for byte in m:
            pm = self.key.ec.kolbitz(byte, self.key.k)
            left = self.key.ec.multiply(self.key.k, self.key.base).to_bytes(block_length)
            right = self.key.ec.add(pm, self.key.ec.multiply(self.key.k, self.key.pub)).to_bytes(block_length)
            encrypted += left+right
        return encrypted

    def decrypt(self, m: bytes):
        if not (self.key and self.key.ec and self.key.base and self.key.k and self.key.pri):
            raise ValueError()
        block_length = math.ceil(self.key.ec.p.bit_length()/8)
        encrypted = [m[i:block_length*4] for i in range(0, len(m), block_length*4)]
        decrypted = ""
        for block in encrypted:
            left = ECCPoint().from_bytes(block[:block_length*2], block_length)
            right = ECCPoint().from_bytes(block[block_length*2:], block_length)

            first = self.key.ec.multiply(self.key.pri, left)
            pm = self.key.ec.add(right, self.key.ec.inv(first))
            decrypted += self.key.ec.decode_kolbitz(pm, self.key.k)
        return decrypted.encode()


if __name__ == '__main__':
    key = ECurve(1, 6, 11)

    p = ECCPoint(2, 4)
    q = ECCPoint(5, 9)


