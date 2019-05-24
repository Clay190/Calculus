#Clay Kynor
#11.19.18

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

func = input("Input your function: ")
num = int(input("Input how many rectangles you want "))
a = float(input("Input the start of your range "))
b = float(input("Input the end of your range "))

#new variable addition to code
integral = float(input("Input the integral of your function from a to b "))

n = (b-a)/num
Ltotal = 0
Mtotal = 0
Rtotal = 0
SimpTotal = 0
y1 = 0
y2 = 0
y3 = 0

for i in range(0,num):
    x=(i*n)+a
    Ltotal += eval(func)*n
    y1 = eval(func)
    x = ((i*n)+a) + (n/2)
    Mtotal += eval(func)*n
    y2 = eval(func)
    x=((i+1)*n)+a
    Rtotal += eval(func)*n
    y3 = eval(func)
    SimpTotal += (y1+(4*y2)+y3)*(n/6)

TrapTotal = (Ltotal+Rtotal)/2

#New code finding the percent error of each method
error1 = abs(((Ltotal - integral)/integral) * 100)
error2 = abs(((Rtotal - integral)/integral) * 100)
error3 = abs(((Mtotal - integral)/integral) * 100)
error4 = abs(((SimpTotal - integral)/integral) * 100)
error5 = abs(((TrapTotal - integral)/integral) * 100)

print("LRAM", Ltotal)
print("MRAM", Mtotal)
print("RRAM", Rtotal)
print("Trapezoid Area", TrapTotal)
print("Simpson's Area", SimpTotal)
print("Percent Error for LRAM is", error1)
print("Percent Error for RRAM is", error2)
print("Percent Error for MRAM is", error3)
print("Percent Error for Trapezoidal Area is", error4)
print("Percent Error for Simpson's Rule is", error5)