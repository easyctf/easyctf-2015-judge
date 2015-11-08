import binascii
import os
import random
import string
import time

TEST_CASE_COUNT = 20

def random_string(l):
    random.seed(time.time() * 128)
    return ''.join(random.choice(string.printable) for _ in range(l))

wtext = []
def encrypt(start, end):
    l = end - start
    print(start, end, l)
    if l == 1:
        return
    encrypt(start, start + l // 2)
    encrypt(start + l // 2, end)
    wtext[start:start + l // 2], wtext[start + l // 2:end] = wtext[start + l // 2:end], wtext[start:start + l // 2]

def generate(full_path):
    try:
        global wtext
        for i in range(10):
            test_case = random_string(random.randint(10 + i * 75, 31 + i * 100))
            wtext = list(test_case)
            encrypt(0, len(wtext))
            test_solution = ''.join(wtext)
            f = open(full_path + os.sep + "test" + str(i) + ".in", "w")
            f.write('e %s' % test_case)
            f.close()
            f = open(full_path + os.sep + "test" + str(i) + ".out", "w")
            f.write(test_solution)
            f.close()
        for i in range(10):
            test_solution = random_string(random.randint(10 + i * 75, 31 + i * 100))
            wtext = list(test_solution)
            encrypt(0, len(wtext))
            test_case = ''.join(wtext)
            f = open(full_path + os.sep + "test" + str(i + 10) + ".in", "w")
            f.write('d %s' % test_case)
            f.close()
            f = open(full_path + os.sep + "test" + str(i + 10) + ".out", "w")
            f.write(test_solution)
            f.close()
        return 1
    except:
        return 0