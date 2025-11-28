#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 08:31:52 2025

@author: xuzikang
"""
class EA_math():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def gcd(self):
        a = self.a
        b = self.b
        while b != 0 and a >= b:
            remainder = a % b
            a = b
            b = remainder
        return a
    def main():
        algo = EA_math(a=9, b=6)
        result = algo.gcd()
        return result