#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:36:17 2025

@author: xuzikang
"""
import my ode
from mymath import EA_math
# create a function
def is_valid_integer(value):
    return value.isdigit() and int(value) > 0


if __name__ == "__main__":
    # let user to write numbers
    A_input = input("Please enter the first positive integer: ")
    B_input = input("Please enter the second positive integer: ")

    # check numbers
    if not (is_valid_integer(A_input) and is_valid_integer(B_input)):
        print("ERROR: Both values must be positive integers!")
    else:
        a = int(A_input)
        b = int(B_input)

        # create EA_math object
        algo = EA_math(a, b)
        result = algo.gcd()

        print(f"The GCD of {a} and {b} is: {result}")
