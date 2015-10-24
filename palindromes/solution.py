#!/usr/bin/env python

from sys import stdin

def find_all_palindromes(str):
  '''
    returns an map, M, of pairs (i, j) to bool
    where M[(i, j)] is true if str[i:j+1] is a palindrome
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

def longest_palindromic_substr(s):
  M = find_all_palindromes(s)

  best = (1,1)
  best_width = 0

  for i, j in (key for key, val in M.iteritems() if val == True):
    width = j - i
    if width > best_width:
      best = (i, j)
      best_width = width
    elif width == best_width and i < best[0]:
      best = (i, j)

  return best

if __name__ == "__main__":
  testcases = int(stdin.readline())

  for _ in range(testcases):
    s = stdin.readline().strip()
    i, j = longest_palindromic_substr(s)
    print("{} {}".format(i, j))
