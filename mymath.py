#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
class EA_math:
    # create a and b
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # the skill of Euclidean Algorithm and define them
    def gcd(self):
        a = self.a
        b = self.b

       
        while b != 0:
            remainder = a % b
            a = b
            b = remainder

        return a