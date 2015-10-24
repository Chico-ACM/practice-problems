#/usr/bin/env python

from collections import namedtuple
import os, errno
from random import seed, choice, randrange
from string import ascii_letters
from hw3 import count_palindromic_substrings

seed(42) # generate the same tests each time

def randstring(length, alphabet = ascii_letters):
    return ''.join((choice(alphabet) for i in xrange(length)))

def mkdir_p(path):
    ''' makes a directory if the directory did not already exist '''
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise


Test = namedtuple("test", "input output")

def make_tests():
    tests = [
        Test("", "0"),
        Test("a", "1"),
        Test("ab", "2"),
        Test("abc", "3"),
        Test("aba", "4"),
        Test("ababa", "9"),
        Test("ababaa", "11")
    ]

    for _ in range(13):
        str = randstring(randrange(2, 30))
        tests.append(Test(str, "{}".format(count_palindromic_substrings(str))))
    for _ in range(20):
        str = randstring(randrange(2, 30), "abcd")
        tests.append(Test(str, "{}".format(count_palindromic_substrings(str))))

    str = "a" * 50
    tests.append(Test(str, "{}".format(count_palindromic_substrings(str))))

    return tests


# write test directory
test_directory = "./tests/"
mkdir_p(test_directory) # create it if it did not already exist

tests = make_tests()
widest_num = len(str(len(tests)))

# write test files
for i, t in enumerate(tests):
    input_filename = "{:0>{width}d}.in".format(i, width = widest_num)
    output_filename = "{:0>{width}d}.out".format(i, width = widest_num)

    with open(test_directory + input_filename, "w+") as input_file:
        input_file.write(t.input)

    with open(test_directory + output_filename, "w+") as output_file:
        output_file.write(t.output)
