from Key.ECurve import *
from Key.ECKey import *


class ECEG:
    def __init__(self, key: ECKey):
        self.key = key

    def encrypt(self, m: bytes):
        n_points = self.key.ec.n_points()
        if n_points < 256:
            raise ValueError()

    def decrypt(self, m: bytes):
        pass


if __name__ == '__main__':
    key = ECurve()
    key.a = 1
    key.b = 6
    key.p = 11

    p = ECCPoint(2, 4)
    q = ECCPoint(5, 9)


