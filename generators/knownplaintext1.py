import binascii
import os
import random
import string

TEST_CASE_COUNT = 20

def random_string(l):
    random.seed()
    return ''.join(random.choice(string.printable) for _ in range(l))

def encrypt(text):
    encoded = str(binascii.hexlify(bytes(text, 'Latin-1')), 'ascii')
    encrypted = ''
    for i in range(len(encoded)):
        encrypted += chr(ord(encoded[i]) + (i % 2))
    return encrypted

def generate(full_path):
    try:
        for i in range(10):
            test_case = random_string(32)
            test_solution = encrypt(test_case)
            f = open(full_path + os.sep + "test" + str(i) + ".in", "w")
            f.write('e %s' % test_case)
            f.close()
            f = open(full_path + os.sep + "test" + str(i) + ".out", "w")
            f.write(test_solution)
            f.close()
        for i in range(10):
            test_solution = random_string(32)
            test_case = encrypt(test_solution)
            f = open(full_path + os.sep + "test" + str(i + 10) + ".in", "w")
            f.write('d %s' % test_case)
            f.close()
            f = open(full_path + os.sep + "test" + str(i + 10) + ".out", "w")
            f.write(test_solution)
            f.close()
        return 1
    except:
        return 0