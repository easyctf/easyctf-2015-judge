import binascii
import os
import random
import string

TEST_CASE_COUNT = 20

def random_string(l):
    return ''.join(random.choice(string.ascii_letters) for _ in range(l))

substitution = {'z': 'P', 'T': 't', 'V': 'J', 'x': 'b', 'g': 'F', 'X': 'Y', 'f': 'e', 'e': 'E', 'W': 'x', 'Q': 'p', 'H': 'D', 'P': 'q', 's': 'Z', 'l': 'u', 'N': 'n', 'E': 'g', 'o': 'i', 'n': 'c', 'Y': 'o', 'G': 'G', 'O': 'Q', 'I': 'O', 'S': 'H', 'h': 'w', 'D': 'y', 'v': 'X', 'w': 's', 'U': 'f', 'p': 'l', 'A': 'C', 't': 'U', 'Z': 'S', 'L': 'B', 'j': 'T', 'a': 'h', 'm': 'A', 'c': 'M', 'y': 'j', 'M': 'L', 'C': 'K', 'b': 'v', 'i': 'd', 'q': 'a', 'r': 'k', 'F': 'z', 'J': 'I', 'u': 'r', 'R': 'm', 'B': 'W', 'd': 'R', 'K': 'V', 'k': 'N'}

def encrypt(text):
    return ''.join([substitution[c] for c in text])

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
            f = open(full_path + os.sep + "test" + str(i) + ".in", "w")
            f.write('d %s' % test_case)
            f.close()
            f = open(full_path + os.sep + "test" + str(i) + ".out", "w")
            f.write(test_solution)
            f.close()
        return 1
    except:
        return 0