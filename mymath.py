#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:31:52 2025

@author: xuzikang
"""
#create a class
class EA_math():
#create a function that put a and b into it
    def __init__(self, a, b):
        self.a = a
        self.b = b
#create a function that include the method of Euclidean Algorithm
    def gcd(self):
        a = self.a
        b = self.b
#when b is not 0 and a more than or equal b and the code can run and it is a loop that continues until b equals 0 or a is less than b
        while b != 0 and a >= b:
#calculate the remainder of a and b
            remainder = a % b
#the length of a equal the last b
            a = b
#the length of b equal the remainder that be calculated in the last time
            b = remainder
        return a
    def main():
#input the value of a and b
        algo = EA_math(a=9, b=6)
        result = algo.gcd()
        return result