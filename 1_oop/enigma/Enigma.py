import os
from main import Enigma

# so that we can just call them without needing to know where they actually are
os.chdir(os.path.dirname(__file__))


def encipher(seed: any, bytes: bytes):
    e = Enigma(seed)
    encoded_buffer = bytearray()

    for b in bytes:
        encoded_byte = e.encipher(b)
        encoded_buffer.append(encoded_byte)

    return encoded_buffer


def main():
    s = "test"
    data = bytearray(s.encode('UTF-8'))
    ciphertext = encipher(100, data)
    print(ciphertext)

    plaintext = encipher(100, ciphertext)
    print(plaintext)


if __name__ == "__main__":
    main()
