#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
numberOfSwaps = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break
print "Array is sorted in %d swaps."  %numberOfSwaps
print "First Element: %d" %a[0]
print "Last Element: %d" %a[-1]
