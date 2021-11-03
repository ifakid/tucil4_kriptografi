from ECurve import *
import json


# ECDH
class ECKey:
    def __init__(self, ec: ECurve, base: ECCPoint):
        self.pub = None
        self.pri = None
        self.kab = None
        self.ec = ec
        self.base = base

    def generate_key(self, pri):
        self.pri = pri
        self.pub = self.ec.multiply(pri, self.base)

    def secret_key(self, other: ECCPoint):
        self.kab = self.ec.multiply(self.pri, other)

    def import_pub_key(self, path):
        if path.split('.')[-1] != 'pub':
            raise ValueError()
        data = json.load(path)
        self.pub = ECCPoint(data['p']['x'], data['p']['y'])

    def import_pri_key(self, path):
        if path.split('.')[-1] != 'pri':
            raise ValueError()
        data = json.load(path)
        self.pri = data['p']

    def export_pub_key(self, path):
        if path.split('.')[-1] != 'pub':
            path += '.pub'
        data = {
            'p': {
                'x': self.pub.x,
                'y': self.pub.y
            }
        }
        with open(path, 'w') as f:
            json.dump(data, f)

    def export_pri_key(self, path):
        if path.split('.')[-1] != 'pri':
            path += '.pri'
        data = {
            'p': self.pri,
        }
        with open(path, 'w') as f:
            json.dump(data, f)
