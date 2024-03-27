from sympy import nextprime
from Crypto.Util.number import inverse
from sage.all import crt
import sys

ints = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
p = 851
while p < 999:
    p = nextprime(p)
    A = []
    for i in range(len(ints) -1):
            a = inverse(ints[i], p)
            A.append(a * ints[i+1])
    try:
        x = crt(A, [p]*(len(A)))
        print(x)
        print(p)
        break
    except:
        pass