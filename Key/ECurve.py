import random
import math


class ECCPoint:
    def __init__(self, x: int = None, y: int = None):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}; y: {self.y}'

    def to_bytes(self, byte_len):
        x = self.x.to_bytes(byte_len, byteorder='big')
        y = self.y.to_bytes(byte_len, byteorder='big')
        return x + y

    def from_bytes(self, b: bytes, byte_len):
        self.x = int.from_bytes(b[:byte_len], byteorder='big')
        self.y = int.from_bytes(b[byte_len:], byteorder='big')


class ECurve:
    # x^3 + ax + b mod p
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.points = []

    def generate_k(self):
        return random.randint(1, self.p - 1)

    def kolbitz(self, m: int, k: int):
        if m >= 256 or m < 0:
            raise ValueError()
        y2 = None
        b = 1
        while True:
            x = (m * k) + b
            y2 = self.calc_y2(x)
            sq = math.sqrt(y2)
            if math.floor(sq) == sq:
                return ECCPoint(x, int(sq))
            b += 1

    def decode_kolbitz(self, p: ECCPoint, k: int):
        x = p.x
        m = (x-1)//k
        return chr(m)

    def find_points(self):
        gf = [(i ** 2) % self.p for i in range(self.p)]
        for x in range(self.p):
            y2 = self.calc_y2(x)
            matches = [i for i, x in enumerate(gf) if x == y2]
            if matches:
                for match in matches:
                    self.points.append(ECCPoint(x, match))

    def n_points(self):
        if not self.points:
            self.find_points()
        return len(self.points)

    def is_valid(self, p: ECCPoint):
        left = (p.y ** 2) % self.p
        right = self.calc_y2(p.x)
        return left == right

    def calc_y2(self, x):
        return (x ** 3 + self.a * x + self.b) % self.p

    def add(self, p: ECCPoint, q: ECCPoint):
        if p.x == q.x:
            m = (((3 * pow(p.x, 2) + self.a) % self.p) * pow(2 * p.y, -1, self.p)) % self.p
        else:
            m = (((q.y - p.y) % self.p) * pow(q.x - p.x, -1, self.p)) % self.p
        print(m)
        new_x = (m ** 2 - p.x - q.x) % self.p
        new_y = (m * (p.x - new_x) - p.y) % self.p
        return ECCPoint(new_x, new_y)

    def multiply(self, n, p: ECCPoint):
        r = ECCPoint(p.x, p.y)
        for _ in range(n - 1):
            r = self.add(r, p)
        return r

    def inv(self, p: ECCPoint):
        return ECCPoint(p.x, pow(p.y, -1, self.p))


if __name__ == '__main__':
    conf = ECurve()
    conf.a = -1
    conf.b = 188
    conf.p = 751
    conf.find_points()
    print(len(conf.points))
