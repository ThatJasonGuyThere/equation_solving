# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:35:23 2016

Solving

t_1 = 0.693*R_a*C
t_2 = (R_a*R_b)/(R_a + R_b) * C * ln((R_b- 2*R_a)/(2*R_b-R_a))
f = 1/(t_1 + t_ 2)

@author: ngj
"""
from scipy.optimize import brentq
import numpy as np
import math

def test_func(R_a):
    return lambda R_b: 0.693*(R_a/R_b) + 0.693 - math.log((R_b - 2*R_a)/(2*R_b - R_a))
    
freq = 1000 #Hz
t_1 = (1/freq)/2
C = np.array([10E-9, 12E-9, 15E-9])
for cap in C:
    R = t_1/(0.693*cap)
    f = test_func(R)
    print('\nC = ' + format(cap) + 'F')
    R_b = brentq(f, 1000, R/2.1)
    print('R_a = ' + format(R, '0.0f') + ' Ohm')
    print('R_b = ' + format(R_b, '0.0f') + ' Ohm')
    t_1 = 0.693*R*cap
    t_2 = (R*R_b)/(R + R_b) * cap * math.log((R_b- 2*R)/(2*R_b-R))
    print('t_1 = ' + format(t_1) + 's, t_2 = ' + format(t_2))
    print('duty = ' + format(t_1/(t_1+t_2)))
    print('freq = ' + format(1/(t_1 + t_2)))
