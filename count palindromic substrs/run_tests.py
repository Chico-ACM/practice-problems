#!/usr/bin/env python

from __future__ import print_function
from sys import argv
from collections import namedtuple
from subprocess import check_output
from os import listdir

program = argv[1] if len(argv) >= 2 else "hw3.py"
test_directory = "./tests/"

print("testing program {} using tests from {}:".format(program, test_directory))

tests = [s for s in listdir(test_directory) if s.endswith(".in")]

print(tests)

num_passed = 0
for i, test_name in enumerate(tests):
	input_filename = test_directory + test_name
	output_filename = "{}.out".format(input_filename[:-3])

	# print progress
	print("test '{}': ".format(test_name, len(tests)), end="")

	# ansi escape code for term coloring
	OKGREEN = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	# output strings
	PASSED = OKGREEN + "Passed" + ENDC
	FAILED = FAIL + "Failed" + ENDC

	# run the program on the test input
	test_output = check_output([program, input_filename]).strip()
	expected_output = open(output_filename).read().strip()

	# print results
	if test_output == expected_output:
		num_passed += 1
		print(PASSED)
	else:
		print(FAILED)
		print("expected '{}', got '{}'\n".format(expected_output, test_output))

print("\nPassed {}/{} tests.".format(num_passed, len(tests)))
