#!/usr/bin/env python

# CSCI 498 hw3
# Author: Lao Akili
# Description:
  # reads in a file specified by the first command line argument
  # and prints to stdout the count of substrings of that file which are palindromes
  # uses the n^2 dynamic programming solution discussed in class

from sys import argv, exit

def find_all_palindromes(str):
  '''
    returns an map, M, of pairs (i, j) to bool
    where M[(i, j)] is true if str[i:j] is a palindrome
    for all valid integers i, j st. 0 <= i <= j <= len(str)
  '''
  M = {}

  # for each substr range, in diagonal order, mark if palindrome
  for width in range(len(str)):
    for start in range(len(str) - width):
      i, j = start, start + width
      substr_len = 1 + width
      if substr_len == 1:
        M[(i, j)] = True
      elif substr_len == 2:
        M[(i, j)] = str[i] == str[j] 
      else: # substr_len is 3 or more characters
        M[(i, j)] = str[i] == str[j] and M[(i + 1, j - 1)]

  return M


def count_palindromic_substrings(str):
  return sum(1 for v in find_all_palindromes(str).values() if v == True)


if __name__ == "__main__":

  if len(argv) != 2:
    print("usage {} <filename>".format(argv[0]))
    exit()

  # get file contents
  str = open(argv[1]).read()

  # print answer
  print(count_palindromic_substrings(str))
