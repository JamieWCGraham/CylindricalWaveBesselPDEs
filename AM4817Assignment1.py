#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:24:03 2021

@author: jamiegraham
"""


import numpy as np 
import matplotlib.pyplot as plt 
import scipy as scipy
import math as math
from scipy import special
from mpl_toolkits import mplot3d

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# first three roots of zeroth order bessel equation



root1 = 2.4048
root2 = 5.5201
root3 = 8.6537

rootlist = [root1,root2,root3]
c = 1 

# computing the summation for the fourier coefficient 

gammalist = []
for i in range(0,3):
    summation = 0
    for n in range(0,20):
        summand = ((-1)**n * (rootlist[i]/2)**(2*n) * ( 1/(2*n+2) - 3/(2*n+4) + 3/(2*n+6) - 1/(2*n+8) ) ) / ((factorial(n))**2) 
        summation = summation + summand
    gammalist.append(summation)
    
    


def solution(r,t):
    
    solution = 0
    for i in range(0,3):
        solution += (2*gammalist[i] * np.cos(rootlist[i]*t) * scipy.special.jn(0,rootlist[i]*r) )  / (scipy.special.jn(1,rootlist[i]))**2
        
    
    return solution




for time in range(0,100):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Create the mesh in polar coordinates and compute corresponding Z.
    r = np.linspace(0, 1, 50)
    p = np.linspace(0, 2*np.pi, 50)
    R, P = np.meshgrid(r, p)

    
    Z = solution(R,time/10)
    
    # Express the mesh in the cartesian system.
    X, Y = R*np.cos(P), R*np.sin(P)
    
    # Plot the surface.
    ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
    
    # Tweak the limits and add latex math labels.
    ax.set_zlim(0, 1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.title("u(r,$\Theta$,t) for t = " + str(round(time/30,2)) + " seconds")
    plt.savefig(str(time) + "u for t = " + str(round(time/30,2)) + " seconds" + ".png")
    plt.show()

