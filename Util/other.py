def size_in_bits(n):
    bits = 0
    while n > 0:
        bits += 1
        n >>= 1
    return bits


if __name__ == '__main__':
    print(size_in_bits(128))