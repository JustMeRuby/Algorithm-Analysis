# -*- coding: utf-8 -*-
"""PTTT - Lab03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Sz9uxhXsgAPiae8hf9pyT2Mu5HmKBXz
"""

from random import randint
import math
import numpy as np
import matplotlib.pyplot as plt
import time

N = range(1024, 2049, 56)

A = list()
B = list()
for n in N:
  a = randint(10 ** (n - 1), 10 ** n - 1)
  b = randint(10 ** (n - 1), 10 ** n - 1)
  A.append(a)
  B.append(b)

def traditional_multiply(A, B):
  result = 0
  for i in range(len(A)):
    num1 = A[i]
    for j in range(len(B)):
      num2 = B[j]
      result = result + int(num1) * int(num2) * 10 ** ((len(A) - 1 - i) + (len(B) - 1 - j))
  return result

time_traditional = list()
result_traditional = list()
for a, b in zip(A, B):
  start_time = time.time()
  result_traditional.append(traditional_multiply(str(a), str(b)))
  time_traditional.append(time.time() - start_time)

def karatsuba(A, B):
  if (int(A) < 10 or int(B) < 10):
    return int(A) * int(B)
  
  split = math.ceil(min(len(A), len(B)) / 2)
  high1, low1 = A[:-split], A[-split:]
  high2, low2 = B[:-split], B[-split:]
  
  z0 = karatsuba(low1, low2)
  z1 = karatsuba(str(int(high1) + int(low1)), str(int(high2) + int(low2)))
  z2 = karatsuba(high1, high2)

  return (z2 * 10 ** (split * 2)) + ((z1 - z2 - z0) * 10 ** split) + z0

time_karatsuba = list()
result_karatsuba = list()
for a, b in zip(A, B):
  start_time = time.time()
  result_karatsuba.append(karatsuba(str(a), str(b)))
  time_karatsuba.append(time.time() - start_time)

plt.figure(figsize=(8, 8))
plt.subplot(221)
plt.plot(N, [i ** math.log2(3) for i in N], label = "N^log2(3)")
plt.legend()
plt.subplot(222)
plt.plot(N, time_karatsuba, label = "Karatsuba Algorithm")
plt.legend()
plt.subplot(223)
plt.plot(N, [i ** 2 for i in N], label = "N^2")
plt.legend()
plt.subplot(224)
plt.plot(N, time_traditional, label = "Traditional Algorithm")
plt.legend()
plt.show()

plt.figure(figsize=(16, 8))
plt.subplot(121)
plt.plot(N, [i ** math.log2(3) for i in N], label = "N^log2(3)")
plt.plot(N, [i ** 2 for i in N], label = "N^2")
plt.legend()
plt.subplot(122)
plt.plot(N, time_karatsuba, label = "Karatsuba Algorithm")
plt.plot(N, time_traditional, label = "Traditional Algorithm")
plt.legend()
plt.show()