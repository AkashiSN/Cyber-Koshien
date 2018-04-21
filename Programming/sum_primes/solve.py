#!/usr/bin/env python
import math

def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3 or x == 5: return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False

    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False

        prime += step
        step = 6 - step

    return True

sum_prime = 0
i = 2
num_prime = 0

while 1:
    if num_prime > 31337:
        break
    if is_prime(i):
        num_prime　+=　1
        if 12345 <= num_prime <= 31337:
            sum_prime += i
    i　+=　1
print sum_prime