#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:31:52 2025

@author: xuzikang
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