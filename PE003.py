# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:53:54 2019

@author: Dipanjan Chowdhury
"""

import math


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def main():
    number = 600851475143
    print(prime_factors(number))


if __name__ == "__main__":
    main()
