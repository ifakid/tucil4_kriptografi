import random


def pkcs1_pad(data: bytes, block_size):
    c_len = len(data)
    p_len = block_size - 3 - c_len
    padding = nonzero_byte() * p_len
    return b'\x00\x02' + padding + b'\x00' + data


def pkcs1_unpad(data: bytes):
    if data[0] != b'\x00' or data[1] != b'\x02':
        raise ValueError()
    return data.split(b'\x00', 2)[-1]


def pkcs7_pad(data: bytes, block_size):
    p_len = block_size - len(data)
    padding = p_len.to_bytes(1, byteorder='big') * p_len
    return data+padding


def pkcs7_unpad(data: bytes):
    p_len = data[-1]
    if data[-p_len:] != p_len.to_bytes(1, byteorder='big') * p_len:
        raise ValueError()
    return data[:-p_len]


def nonzero_byte():
    b = random.getrandbits(8)
    while b == 0x00:
        b = random.getrandbits(8)
    return b.to_bytes(1, byteorder='big')