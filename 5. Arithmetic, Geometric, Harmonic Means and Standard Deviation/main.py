# Author: Xavier Lopez
# Date Started: 5/18/2022
# Date Finished: 5/18/2022

#
# Description:
# Write a Python program that will ask the user to enter
#   5 integers, then print the numbers from greatest to least,
#   and calculate the arithmetic mean, geometric mean, harmonic
#   mean and standard deviation
#

from math import *

A, B, C, D, E = input("Enter five numbers: ").split()
a = int(A)
b = int(B)
c = int(C)
d = int(D)
e = int(E)
print("")
print("")
print("")

if a < b:
    temp = a
    a = b
    b = temp

if a < c:
    temp = a
    a = c
    c = temp

if a < d:
    temp = a
    a = d
    d = temp

if a < e:
    temp = a
    a = e
    e = temp

if b < c:
    temp = b
    b = c
    c = temp

if b < d:
    temp = b
    b = d
    d = temp

if b < e:
    temp = b
    b = e
    e = temp

if c < d:
    temp = c
    c = d
    d = temp

if c < e:
    temp = c
    c = e
    e = temp

if d < e:
    temp = d
    d = e
    e = temp

arith_mean = (a + b + c + d + e) / 5.0
geo_mean = pow((a * b * c * d * e), (1.0/5))
harm_mean = 5.0 / ((1/a) + (1/b) + (1/c) + (1/d) + (1/e))
stan_dev = sqrt((pow(a - arith_mean, 2) +
                 pow(b - arith_mean, 2) +
                 pow(c - arith_mean, 2) +
                 pow(d - arith_mean, 2) +
                 pow(e - arith_mean, 2)) / 5.0)

print("Result:\n")
print("Data:")
print(a)
print(b)
print(c)
print(d)
print(e)
print("")
print("Arithmetic Mean    = " + ('%.2f' % arith_mean))
print("Geometric  Mean    = " + ('%.2f' % geo_mean))
print("Harmonic   Mean    = " + ('%.2f' % harm_mean))
print("Standard Deviation = " + ('%.2f' % stan_dev))
